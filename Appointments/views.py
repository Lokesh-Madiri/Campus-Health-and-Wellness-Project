from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random

@login_required
def appointments_form(request):
    if request.method == "POST":
        date = request.POST["date"]
        description = request.POST["message"]

        # Select a random doctor
        doctors = User.objects.filter(userprofile__role="Doctor")
        doctor = random.choice(doctors) if doctors.exists() else None

        # Create an appointment and assign a doctor
        appointment = Appointment.objects.create(
            user=request.user,
            doctor=doctor,
            date=date,
            description=description,
            status="Pending"
        )

        messages.success(request, f"Appointment booked successfully! Assigned Doctor: {doctor.username if doctor else 'None'}")

    return render(request, 'appointments_form.html')


@login_required
def manage_appointments(request):
    if request.user.userprofile.role.lower() != "doctor":
        return redirect("homepage")

    # Fetch only the appointments assigned to the logged-in doctor
    appointments = Appointment.objects.filter(doctor=request.user)

    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        status = request.POST.get("status")

        appointment = Appointment.objects.get(id=appointment_id, doctor=request.user)
        appointment.status = status
        appointment.save()

        messages.success(request, "Appointment updated successfully!")
        return redirect("manage_appointments")

    return render(request, "manage_appointments.html", {"appointments": appointments})


@login_required
def cancel_appointment(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id, user=request.user)
        appointment.status = "Cancelled"
        appointment.save()
        messages.info(request, "Appointment cancelled successfully.")
    except Appointment.DoesNotExist:
        messages.error(request, "Invalid appointment or unauthorized access.")
        
    return redirect("userdashboard")

@login_required
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Ensure only the assigned doctor can view/manage it
    if request.user.userprofile.role.lower() != "doctor":
        messages.error(request, "Unauthorized access!")
        return redirect("accounts:doctordashboard")

    if request.method == "POST":
        status = request.POST.get("status")
        appointment.status = status
        appointment.save()
        messages.success(request, "Appointment status updated successfully!")
        return redirect("accounts:doctordashboard")

    return render(request, "appointment_detail.html", {"appointment": appointment})