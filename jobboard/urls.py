from django.contrib import admin
from django.urls import path, include
from jobs import views  

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')), 
]
