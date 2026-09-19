"""
Tanpa ModelForm, jika kita punya model dengan 20 kolom (misal: nama, email, alamat, dll.), 
Kita harus mengetik 20 kolom itu tiga kali: di berkas models.py, di forms.py, dan validasinya di views.py.
Dengan ModelForm, Anda cukup menulisnya satu kali di models.py. Formulir HTML akan langsung menyesuaikan 
jenisnya (teks, angka, atau tanggal). Jika ada kolom angka, formulir otomatis menolak jika pengguna memasukkan huruf.
kita tidak perlu menulis kode pengecekan (if-else) satu per satu untuk setiap kolom.
Dengan ModelForm, Django langsung membaca, memvalidasi, dan menyimpannya ke basis data hanya dengan perintah .save():


"""
from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput

from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "technology",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Posisi / Judul Pengalaman",
            "description": "Deskripsi Pekerjaan / Peran",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Thumbnail",
            "ended_at": "Tanggal Selesai (Opsional)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "cth: Software Engineer Intern",
                    "maxlength": 255,
                    "class": "w-full rounded-md border border-gray-300 p-2 focus:ring-indigo-500 focus:border-indigo-500",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Jelaskan tanggung jawab dan pencapaianmu...",
                    "rows": 4,
                    "class": "w-full rounded-md border border-gray-300 p-2 focus:ring-indigo-500 focus:border-indigo-500",
                }
            ),
            "category": Select(
                attrs={
                    "class": "w-full rounded-md border border-gray-300 p-2 focus:ring-indigo-500 focus:border-indigo-500",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://example.com/logo.png",
                    "class": "w-full rounded-md border border-gray-300 p-2 focus:ring-indigo-500 focus:border-indigo-500",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                    "class": "w-full rounded-md border border-gray-300 p-2 focus:ring-indigo-500 focus:border-indigo-500",
                }
            ),
        }