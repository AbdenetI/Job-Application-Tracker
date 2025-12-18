from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('applications/', views.application_list, name='application_list'),
    path('applications/add/', views.application_create, name='application_create'),
    path('applications/<int:pk>/', views.application_detail, name='application_detail'),
    path('applications/<int:pk>/edit/', views.application_update, name='application_update'),
    path('applications/<int:pk>/status/', views.application_status_update, name='application_status_update'),
    path('companies/add/', views.company_create, name='company_create'),
    path('jobs/add/', views.job_create, name='job_create'),
]
