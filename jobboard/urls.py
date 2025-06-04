from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),  # 👈 all views are now handled in jobs/urls.py
]


