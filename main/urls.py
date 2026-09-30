from django.urls import path

from main.views import show_main, show_experience, show_projects, create_project, edit_project, delete_project, show_experience, create_experience, edit_experience, delete_experience, show_json, show_json_by_id, register, login_user, logout_user, toggle_star, get_projects_json, create_project_ajax

app_name = "main"

urlpatterns = [
    # path yg sudah dibuat di tutorial 2 utk experience
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    # path untuk projects
    path('projects/', show_projects, name='show_projects'),
    path("projects/add/", create_project, name="create_project"),
    path('projects/edit/<int:id>/', edit_project, name='edit_project'),
    path('projects/delete/<int:id>/', delete_project, name='delete_project'),
    # path untuk tugas 3 punya experience
    path('experience/create/', create_experience, name='create_experience'),
    path('experience/edit/<str:id>/', edit_experience, name='edit_experience'),
    path('experience/delete/<str:id>/', delete_experience, name='delete_experience'),
    path('experience/json/', show_json, name='show_json'),
    path('experience/json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    # path untuk tutorial 4, login logout
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<int:project_id>/star/", toggle_star, name="toggle_star"),
    path('api/projects/', get_projects_json, name='get_projects_json'),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax")
]