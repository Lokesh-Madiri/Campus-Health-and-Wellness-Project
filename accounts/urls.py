from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import add_disease

app_name = 'accounts'

urlpatterns = [
     path('login/', views.login, name='login'), 
     path('registration/', views.registration, name='registration'),
     path('userdashboard/', views.userdashboard, name='userdashboard'),
     path('logout/', auth_views.LogoutView.as_view(next_page='homepage:home'), name='logout'),
     path('doctordashboard/', views.doctor_dashboard, name='doctordashboard'),
     path('coordinatordashboard/', views.coordinator_dashboard, name='coordinatordashboard'),
     path('add_disease/', add_disease, name='add_disease'),
]
