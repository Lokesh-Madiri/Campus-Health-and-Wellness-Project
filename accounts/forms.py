from django import forms
from HealthHive.models import Disease

class DiseaseForm(forms.ModelForm):
    featured = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    class Meta:
        model = Disease
        fields = ['name', 'description', 'image','featured']
