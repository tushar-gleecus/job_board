from django.urls import path
from .views import (
    JobListView, JobDetailView, JobCreateView,
    JobUpdateView, JobDeleteView, apply_to_job
)

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/edit/', JobUpdateView.as_view(), name='job_edit'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('<int:pk>/apply/', apply_to_job, name='job_apply'),
]
