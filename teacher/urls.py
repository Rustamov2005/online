from django.urls import path
from .views import teacher, login, register

urlpatterns = [
    path('teacher/', teacher, name='teacher'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]