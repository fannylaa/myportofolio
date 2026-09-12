# Create your views here.
"""
penjelasan alur pengolahan data django (mvt arch dan penambahan new fitur): 

setiap kali menambahkan fitur/model baru pada django, urutan proses yang terjadi adalah:

1. url routing (main/urls.py):
   mengatur 'pintu masuk' atau alamat web. memetakan url request dari browser 
   ke fungsi handler yang sesuai di `views.py`.
   (contoh pada fitur ini: memetakan url '/projects/' ke fungsi `show_projects`).

2. logika view dan model (main/views.py & main/models.py):
   fungsi view dipanggil untuk memproses logika bisnis dan mengambil data dari 
   database melalui model (`Model.objects.all()`). data yang di input via 
   django ddmin (main/admin.py) ditarik di tahap ini.
   (contoh pada fitur ini: `show_projects` mengambil semua data `Project`).

3. contect dan templatee (main/views.py & main/templates/...):
   data dari model dimasukkan ke dalam dictionary `context`, lalu diteruskan ke 
   template html untuk dirender menjadi halaman web dinamis.
   (contoh pada fitur ini: menyalurkan `context` ke template `projects.html`).

"""
from django.shortcuts import render

from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Stephanie",
        "npm": "2506547153",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    experiences = Experience.objects.all()

    context = {
        'name': 'Stephanie',
        'experiences': experiences,
    }
    return render(request, 'experience.html', context)

def show_projects(request):
    """
    View untuk mengambil seluruh objek Project dari database 
    dan mengalirkannya ke template projects.html lewat context.
    """
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'projects': projects,
    }
    return render(request, 'projects.html', context)