from django.urls import path
from .views import SpecialityCreateView, SpecialityUpdateView, SpecialityDeleteView

urlpatterns = [
    path('speciality/add/', SpecialityCreateView.as_view(), name='speciality_add'),
    path('speciality/<int:pk>/edit/', SpecialityUpdateView.as_view(), name='speciality_edit'),
    path('speciality/<int:pk>/delete/', SpecialityDeleteView.as_view(), name='speciality_delete'),

]
