from django.shortcuts import render
from HealthHive.models import Disease
from django.shortcuts import render, get_object_or_404
# Create your views here.

def search_results(request):
    query = request.GET.get('query')
    diseases = Disease.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'diseases': diseases})

def disease_detail(request, disease_id):
    disease = get_object_or_404(Disease, id=disease_id)
    return render(request, 'disease_detail.html', {'disease': disease})