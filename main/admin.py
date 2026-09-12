from django.contrib import admin
from .models import Experience, Project

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'started_at', 'status_text')
    list_filter = ('category',)

    search_fields = ('title', 'description')
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # Menentukan kolom apa saja yang tampil di list tabel Django Admin
    list_display = ('title', 'technology', 'created_at')
    # Menentukan kolom mana saja yang bisa dicari via pencarian Admin
    search_fields = ('title', 'technology', 'description')