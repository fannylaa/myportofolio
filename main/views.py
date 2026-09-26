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

import datetime
from main.models import Experience, Project
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from main.forms import ProjectForm
from main.forms import ExperienceForm
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Stephanie",
        "npm": "2506547153",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    query = request.GET.get('q', '')
    if query:
        # Sesuaikan 'role' atau 'company' dengan field yang ada di model Experience kamu
        experiences = Experience.objects.filter(title__icontains=query) | Experience.objects.filter(description__icontains=query)
    else:
        experiences = Experience.objects.all()

    context = {
        'name': 'Stephanie',
        'selected_query': query,
        'experiences': experiences,
    }
    return render(request, 'experience.html', context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience') 
    
    context = {'form': form, 'name': 'Stephanie'}
    return render(request, 'create_experience.html', context)

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
        
    context = {'form': form, 'name': 'Stephanie'}
    return render(request, 'edit_experience.html', context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')

def show_json(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = Experience.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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
        'name': 'Stephanie',
        'projects': projects,
        'selected_tech': tech_query,
    }
    return render(request, 'projects.html', context)

@login_required(login_url="/login/")
def create_project(request):
    """
    View untuk menangani pembuatan proyek baru melalui form (ModelForm).
    """
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Stephanie",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def edit_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_projects')
        
    context = {'form': form, 'name': 'Stephanie'}
    return render(request, 'edit_project.html', context)

def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect('main:show_projects')

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Stephanie",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response