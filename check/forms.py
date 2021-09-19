from django import forms
from .models import *

class SatDetailForm(forms.ModelForm):
    
    class Meta:
        model = Satellite
        fields = ['satellite', 'sat_id']

class pids_input(forms.ModelForm):
    
    class Meta:
        model = reference_input
        fields = '__all__'

