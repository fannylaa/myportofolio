from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'started_at', 'status_text')
    list_filter = ('category',)
    search_fields = ('title', 'description')