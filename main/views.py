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
    query = request.GET.get('q', '')
    if query:
        # Sesuaikan 'role' atau 'company' dengan field yang ada di model Experience kamu
        experiences = Experience.objects.filter(role__icontains=query) | Experience.objects.filter(company__icontains=query)
    else:
        experiences = Experience.objects.all()

    context = {
        'name': 'Stephanie',
        'selected_query': query,
    }
    return render(request, 'experience.html', context)

def show_projects(request):
    """
    View untuk mengambil seluruh objek Project dari database 
    dan mengalirkannya ke template projects.html lewat context.
    """
    tech_query = request.GET.get('tech', '')
    if tech_query:
        projects = Project.objects.filter(technology__icontains=tech_query)
    else:
        projects = Project.objects.all()

    context = {
        'projects': projects,
        'selected_tech': tech_query,
    }
    return render(request, 'projects.html', context)