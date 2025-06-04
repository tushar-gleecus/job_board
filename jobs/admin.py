# jobs/admin.py

from django.contrib import admin
from .models import Job, Application

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_by', 'created_at')
    search_fields = ('title', 'company')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_at')
    search_fields = ('job__title', 'applicant__username')

admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
