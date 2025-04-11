from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from accounts.models import UserProfile
from Appointments.models import Appointment
from .forms import DiseaseForm

# Create your views here.
from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("homepage:home")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("accounts:login")
    else:
     return render(request, 'loginpage.html')

def registration(request):
     
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        role = request.POST['role']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect("accounts:registration")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect("accounts:registration")
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        user.save()

        UserProfile.objects.create(user=user, role=role)

        return render(request, 'redirect_after_delay.html', {'redirect_url': 'accounts:login'})

    else:
        return render(request, 'registration.html')

@login_required
def userdashboard(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user, defaults={"role": "none"})

    if profile.role == 'Citizen' or profile.role == 'Student':
        
        appointments = Appointment.objects.filter(user=user)
        context = {
            "user": user,
            "profile": profile,
            "appointments": appointments,
            "date": datetime.today().strftime('%Y-%m-%d'),
            "time": datetime.now().strftime('%H:%M'),
        }
        return render(request, 'userdashboard.html', context)

    elif profile.role == 'Doctor':
        
        doctor_appointments = Appointment.objects.filter(doctor=user)
        context = {
            "user": user,
            "profile": profile,
            "appointments": doctor_appointments,
            "date": datetime.today().strftime('%Y-%m-%d'),
            "time": datetime.now().strftime('%H:%M'),
        }
        return render(request, 'doctordashboard.html', context)

    elif profile.role == 'Coordinator':
        return render(request, 'coordinatordashboard.html', {"user": user, "profile": profile , "date" : datetime.today().strftime('%Y-%m-%d') , "time" : datetime.now().strftime('%H:%M')})

    messages.error(request, "Login failed. Please try again.")
    return render(request, 'homepage.html', {"user": user, "profile": profile})

@login_required
def doctor_dashboard(request):
    if request.user.userprofile.role != 'doctor':
        return redirect('/')  
    return render(request, 'doctordashboard.html')

@login_required
def coordinator_dashboard(request):
    if request.user.userprofile.role != 'coordinator':
        return redirect('/')  
    return render(request, 'coordinatordashboard.html')

@login_required
@login_required
def add_disease(request):
    form = DiseaseForm()  # ✅ Initialize form before any condition

    if request.method == 'POST':
        form = DiseaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:coordinatordashboard') 
        else:
            print("Form errors:", form.errors)

    return render(request, 'add_disease.html', {'form': form})
