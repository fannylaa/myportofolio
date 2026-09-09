# Create your views here.
from django.shortcuts import render

from main.models import Experience


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
    # 1. Pastikan nama variabel di sini memakai 's' (experiences)
    experiences = Experience.objects.all()

    context = {
        'name': 'Stephanie',
        'experiences': experiences,
    }
    return render(request, 'experience.html', context)

   