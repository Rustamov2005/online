from django.urls import path
from .views import teacher, login, register, create_teacher, update_teacher, delete_teacher

urlpatterns = [
    path('teacher/', teacher, name='teacher'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('teacher/create/', create_teacher, name='create_teacher'),
    path('teacher/<int:pk>/update/', update_teacher, name='update_teacher'),
    path('teacher/<int:pk>/delete/', delete_teacher, name='delete_teacher'),
]