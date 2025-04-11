from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from HealthHive.models import Disease

# Create your views here.
from django.shortcuts import render

def home(request):
    featured_diseases = Disease.objects.filter(featured=True)[:4]
    print("Featured Diseases:", featured_diseases)
    return render(request, 'Homepage.html', {'featured_diseases': featured_diseases})

