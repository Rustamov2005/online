from django.urls import path
from .views import curseviwe, update_course, create_course, delete_course

urlpatterns = [
    path('curseviwe/', curseviwe, name='curseviwe'),
    path('course/create/', create_course, name='create_course'),
    path('course/<int:pk>/update/', update_course, name='update_course'),
    path('course/<int:pk>/delete/', delete_course, name='delete_course'),
]