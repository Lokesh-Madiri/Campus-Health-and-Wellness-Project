from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import random


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_appointments")  # Patient
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="doctor_appointments")  # Assigned Doctor
    date = models.DateField()
    description = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=[("Confirmed", "Confirmed"), ("Pending", "Pending"), ("Cancelled", "Cancelled")],
        default="Pending"
    )

    def assign_random_doctor(self):
        """Assigns a random doctor from the available doctors."""
        doctors = User.objects.filter(userprofile__role="Doctor")
        if doctors.exists():
            self.doctor = random.choice(doctors)
            self.save()

    def __str__(self):
        return f"{self.user.username} - {self.description} on {self.date} (Doctor: {self.doctor.username if self.doctor else 'Not Assigned'})"
