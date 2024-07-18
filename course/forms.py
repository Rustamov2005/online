from django import forms
from home.models import Courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'students', 'mentor', 'img', 'price', 'rating', 'spesial']
