from django.contrib import admin
from django.urls import path
from . import views

app_name = 'HealthHive'

urlpatterns = [
     path('search/', views.search_results, name='search_results'),
    path('<int:disease_id>/', views.disease_detail, name='disease_detail'),
]