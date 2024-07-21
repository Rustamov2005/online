from django import forms
from home.models import Speciality


class SpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['title', 'img', 'slug']
