from django.shortcuts import render
from main.models import Project

def landing_page(request):
    return render(request, 'index.html')

