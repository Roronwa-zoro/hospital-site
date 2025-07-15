from django.db import models

# Create your models here.
from django.db import models

class MonthlySchedule(models.Model):
    image = models.ImageField(upload_to='schedules/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"جدول المناوبات - {self.uploaded_at.strftime('%Y-%m-%d')}"

class ColdSurgerySchedule(models.Model):
    image = models.ImageField(upload_to='cold_surgery_schedules/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "جدول العمليات الباردة"
