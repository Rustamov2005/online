from django import forms
from home.models import Teachers


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['full_name', 'job_title', 'img', 'social_link_telegram', 'social_link_youtube', 'social_link_linkedin']
