import uuid

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Experience


class ExperienceAPITest(APITestCase):
    """Individual Assignment 6: API Experience dengan empat peran."""

    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.editor = User.objects.create_user(username="editor", password="test-password")
        # Database pengujian selalu kosong, jadi grup Editor dibuat di sini
        self.editor.groups.add(Group.objects.create(name="Editor"))

        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP", description="Membantu praktikum.", category="part-time",
        )
        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse("api:experience-detail", args=[self.experience.id])
        self.star_url = reverse("api:experience-star", args=[self.experience.id])
        self.payload = {
            "title": "Magang Backend", "description": "Membuat API.",
            "category": "internship", "thumbnail": "", "ended_at": None,
        }

    # ---------- membaca ----------
    def test_guest_can_read_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.experience.id))
        self.assertEqual(response.data[0]["category_display"], "Part-Time")
        self.assertTrue(response.data[0]["is_ongoing"])
        self.assertFalse(response.data[0]["is_starred"])
        # data akun sensitif tidak ikut tampil
        self.assertNotIn("starred_by", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_uses_query_parameter(self):
        response = self.client.get(self.list_url, {"q": "dosen"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"q": "praktikum"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"q": "tidak-ada"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_missing_experience_returns_404(self):
        url = reverse("api:experience-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    # ---------- pengunjung dan pengguna biasa ditolak ----------
    def test_guest_and_regular_user_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"title": "X"}, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        # isi database tidak berubah
        self.assertEqual(Experience.objects.count(), 1)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Asisten Dosen PBP")

    # ---------- Editor ----------
    def test_editor_can_patch_and_put_but_not_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)
        response = self.client.patch(self.detail_url, {"title": "Diubah Editor"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Diubah Editor")
        self.assertEqual(self.experience.description, "Membantu praktikum.")

        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Magang Backend")

        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_editor_group_name_must_match(self):
        other = User.objects.create_user(username="other", password="test-password")
        other.groups.add(Group.objects.create(name="Reviewer"))
        self.client.force_authenticate(user=other)
        response = self.client.patch(self.detail_url, {"title": "X"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ---------- pemilik ----------
    def test_owner_can_create_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Experience.objects.filter(pk=response.data["id"]).exists())

        response = self.client.patch(self.detail_url, {"title": "Diubah Pemilik"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_put_requires_all_required_fields(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.put(self.detail_url, {"title": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("description", response.data)

    def test_date_only_ended_at_is_accepted(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"ended_at": "2026-05-01"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data["is_ongoing"])
        self.assertEqual(response.data["status_text"], "Selesai")
        response = self.client.patch(self.detail_url, {"ended_at": None}, format="json")
        self.assertTrue(response.data["is_ongoing"])

    # ---------- validasi ----------
    def test_validation_rejects_bad_input(self):
        self.client.force_authenticate(user=self.owner)
        cases = [
            ({"title": "   "}, "title"),
            ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
            ({"description": "<b></b>"}, "description"),
            ({"category": "bukan-kategori"}, "category"),
            ({"thumbnail": "javascript:alert(1)"}, "thumbnail"),
        ]
        for changes, field in cases:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, field)
            self.assertIn(field, response.data)
        self.assertEqual(Experience.objects.count(), 1)

    def test_text_is_stripped_of_html_tags(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(
            self.list_url, {**self.payload, "title": "Magang <b>Backend</b>"}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Magang Backend")

    # ---------- star ----------
    def test_star_requires_login(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.experience.starred_by.count(), 0)

    def test_regular_user_can_toggle_star(self):
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        self.assertEqual(response.data["starred_by_names"], "visitor")
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_star_uses_request_user_not_body(self):
        self.client.force_authenticate(user=self.visitor)
        self.client.post(self.star_url, {"user": self.owner.id, "starred_by": [self.owner.id]}, format="json")
        self.assertEqual(list(self.experience.starred_by.all()), [self.visitor])

    def test_get_on_star_endpoint_is_not_allowed(self):
        self.client.force_authenticate(user=self.visitor)
        self.assertEqual(self.client.get(self.star_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
            "is_ongoing": False, "status_text": "palsu",
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertTrue(response.data["is_ongoing"])
        created = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(created.starred_by.count(), 0)

    # ---------- CSRF ----------
    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Experience.objects.count(), 1)
        response = client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Experience.objects.filter(pk=self.experience.pk).exists())

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")
        # Browsable API merender token CSRF asli ke dalam response
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
