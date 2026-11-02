from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        Experience.objects.create(
            title="Software Engineering Intern",
            description="Developing web applications.",
            category="Work"

        )
        self.client = Client()
        # Buat dummy data untuk Project
        self.project = Project.objects.create(
            title="Aplikasi Portofolio",
            description="Built using Django MVT architecture.",
            technology="Python & Django",
            project_url="https://github.com/example/portfolio"
        )
        self.project2 = Project.objects.create(
            title="Data Visualizer",
            description="Dashboard for analyzing metrics.",
            technology="React JS"
        )
        
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mengajar praktikum.",
            category="part-time"
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        # Sejak Tutorial 05 halaman ini memuat kartu lewat AJAX, jadi halaman
        # HTML diuji kerangkanya dan datanya diuji lewat API DRF (Tugas 6).
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:experience-list"))
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        data = self.client.get(reverse("api:experience-list")).data
        titles = [item["title"] for item in data]
        self.assertIn(self.experience.title, titles)
        item = next(i for i in data if i["id"] == str(self.experience.id))
        self.assertEqual(item["description"], self.experience.description)
        self.assertEqual(item["category_display"], "Part-Time")
        self.assertEqual(item["status_text"], "Sedang berlangsung")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan")
        self.assertEqual(self.client.get(reverse("api:experience-list")).data, [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
       

    def test_project_model(self):
        self.assertEqual(str(self.project), "Aplikasi Portofolio")
        self.assertEqual(self.project.technology, "Python & Django")

    def test_projects_page(self):
        response = self.client.get(reverse("main:show_projects"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, reverse("api:project-list"))

        # Kartu dirender lewat AJAX, jadi datanya diperiksa di API
        data = self.client.get(reverse("api:project-list")).data
        item = next(i for i in data if i["id"] == self.project.id)
        self.assertEqual(item["title"], self.project.title)
        self.assertEqual(item["description"], self.project.description)
        self.assertEqual(item["project_url"], self.project.project_url)
        self.assertEqual(item["tech_stack"], self.project.technology)

    def test_empty_projects_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(response, "Belum ada proyek yang ditambahkan")
        self.assertEqual(self.client.get(reverse("api:project-list")).data, [])

    def test_main_url_is_exist(self):
        response = self.client.get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_uses_correct_template(self):
        response = self.client.get(reverse('main:show_projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')

    def test_experience_page_uses_correct_template(self):
        response = self.client.get(reverse('main:show_experience'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experience.html')

    def test_project_search_filter(self):
        # Pencarian proyek kini lewat parameter ?title= pada API (Tutorial 07)
        response = self.client.get(reverse('api:project-list'), {'title': 'Portofolio'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual([i['title'] for i in response.data], ["Aplikasi Portofolio"])
       
    def test_experience_search_filter(self):
        # Pencarian pengalaman kini lewat parameter ?q= pada API (Tugas 6)
        response = self.client.get(reverse('api:experience-list'), {'q': 'Intern'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual([i['title'] for i in response.data], ["Software Engineering Intern"])

    def test_empty_search_result(self):
        # Uji pencarian yang tidak ada datanya memicu state kosong
        response = self.client.get(reverse('api:project-list'), {'title': 'NonExistentTech'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])
        page = self.client.get(reverse('main:show_projects'))
        self.assertContains(page, "Belum ada proyek yang ditambahkan")