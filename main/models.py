# Create your models here.
import uuid
from django.db import models
"""
penjelasan: 
1. model (file models.py):
   - representasi struktur data berbasis py
   - sebagai blue print skema tabel database
   - mengatur nama kolom, tipe data, validasi, dan relasi antar tabel

2. migration (folder main/migrations/):
   - penerjemah atau jembatan antara kode py dan sql (database)
   - 'python manage.py makemigrations': membaca perubahan di models.py lalu 
     membuat berkas instruksi (script migrasi) di folder main/migrations/.
   - 'python manage.py migrate': menjalankan instruksi migrasi tersebut untuk 
     membuat/mengubah tabel nyata di dalam database (PostgreSQL/SQLite).

HUBUNGAN KEDUANYA:
- Setiap ada perubahan struktur pada Class Model (misal: tambah field/model baru), 
  file migrasi BARU harus dibuat agar struktur database nyata tetap sinkron 
  dengan rancangan kode py yang kita tulis.

"""
# untuk menyimpan daftar pengalamam, organisasi, akademik, dll
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

    @property
    def status_text(self):
        return "Sedang berlangsung" if self.is_ongoing else "Selesai"

# Model: Projects (Tugas 2)
# Menyimpan data porto proyek yang dibuat
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=255, help_text="Contoh: Java, Python, Django")
    project_url = models.URLField(blank=True, null=True, help_text="Link ke repository/demo")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title