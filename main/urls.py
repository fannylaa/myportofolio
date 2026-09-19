from django.urls import path

from main.views import show_main, show_experience, show_projects, create_project, show_experience, create_experience, edit_experience, delete_experience, show_json, show_json_by_id

app_name = "main"

urlpatterns = [
    # path yg sudah dibuat di tutorial 2 utk experience
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    # path untuk projects
    path('projects/', show_projects, name='show_projects'),
    path("projects/add/", create_project, name="create_project"),
    # path untuk tugas 3 punya experience
    path('experience/create/', create_experience, name='create_experience'),
    path('experience/edit/<str:id>/', edit_experience, name='edit_experience'),
    path('experience/delete/<str:id>/', delete_experience, name='delete_experience'),
    path('experience/json/', show_json, name='show_json'),
    path('experience/json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]