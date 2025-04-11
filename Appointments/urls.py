from django.urls import path
from . import views

app_name = 'Appointments'

urlpatterns = [
    path('appointments_form/', views.appointments_form, name='appointments_form'),
    path('manage_appointments/', views.manage_appointments, name='manage_appointments'),
    path('appointment/<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),  
    path('appointment/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),  # New route for appointment details
]
