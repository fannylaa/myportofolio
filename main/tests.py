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
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

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
        self.assertContains(response, self.project.title, html=True)
        self.assertContains(response, self.project.description, html=True)
        self.assertContains(response, self.project.project_url)
        self.assertContains(response, self.project.technology, html=True)

    def test_empty_projects_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(response, "Belum ada proyek yang ditambahkan.")

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
        # Uji pencarian teknologi 'Django'
        response = self.client.get(reverse('main:show_projects'), {'tech': 'Django'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aplikasi Portofolio")
       
    def test_experience_search_filter(self):
        # Uji pencarian pengalaman 'Intern'``
        response = self.client.get(reverse('main:show_experience'), {'q': 'Intern'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Software Engineering Intern")

    def test_empty_search_result(self):
        # Uji pencarian yang tidak ada datanya memicu state kosong
        response = self.client.get(reverse('main:show_projects'), {'tech': 'NonExistentTech'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada proyek yang ditambahkan.")