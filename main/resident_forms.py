from django import forms
from .models import ResidentInformation

class ResidentInformationForm(forms.ModelForm):
    class Meta:
        model = ResidentInformation
        fields= '__all__'