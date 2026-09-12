from django.urls import path

from main.views import show_main, show_experience, show_projects

app_name = "main"

urlpatterns = [
    # path yg sudah dibuat di tutorial 2 utk experience
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    # path untuk projects
    path('projects/', show_projects, name='show_projects'),
]