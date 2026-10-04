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
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        
from django.http import JsonResponse
from django.views.decorators.http import require_POST

...

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

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
    is_editor = request.user.groups.filter(name='Editor').exists()
    query = request.GET.get('q', '')
    if query:
        # Sesuaikan 'role' atau 'company' dengan field yang ada di model Experience kamu
        experiences = Experience.objects.filter(title__icontains=query) | Experience.objects.filter(description__icontains=query)
    else:
        experiences = Experience.objects.all()

    context = {
        'name': 'Stephanie',
        'selected_query': query,
        'is_editor': is_editor,
        'experiences': experiences,
        "form": ExperienceForm(),
    }
    return render(request, 'experience.html', context)

def create_experience(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Maaf, hanya pemilik portofolio yang dapat menambahkan experience baru.")
        
    form = ExperienceForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience') 
    
    context = {'form': form, 'name': 'Stephanie'}
    return render(request, 'create_experience.html', context)

def edit_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        return HttpResponseForbidden("Anda tidak memiliki hak akses untuk mengubah data experience ini.")

    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')
        
    context = {'form': form, 'name': 'Stephanie'}
    return render(request, 'edit_experience.html', context)

def delete_experience(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Maaf, hanya pemilik portofolio yang dapat menghapus data experience.")
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
    is_editor = request.user.groups.filter(name='Editor').exists()
    
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Stephanie",
        "is_editor": is_editor,
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)

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
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor):
        return HttpResponseForbidden("Anda tidak memiliki hak akses untuk mengubah data ini.")
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_projects')
        
    context = {'form': form, 'name': 'Stephanie'}
    return render(request, 'edit_project.html', context)

def delete_project(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Maaf, hanya pemilik portofolio (superuser) yang dapat menghapus proyek.")
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

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.technology,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def get_experiences_json(request):
    query = request.GET.get("q", "").strip()
    experiences = Experience.objects.all()

    if query:
        experiences = experiences.filter(title__icontains=query) | experiences.filter(description__icontains=query)

    data = []
    for exp in experiences:
        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "description": exp.description,
                "category": exp.category,
                "thumbnail": exp.thumbnail or "",
                "started_at": exp.started_at.strftime("%Y-%m-%d %H:%M"),
                "ended_at": exp.ended_at.strftime("%Y-%m-%d") if exp.ended_at else None,
                "is_ongoing": exp.is_ongoing,
                "status_text": exp.status_text,
            }
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)