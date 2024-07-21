from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from home.models import Speciality
from .forms import SpecialityForm


class SpecialityCreateView(CreateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'speciality_form.html'
    success_url = reverse_lazy('speciality_list')


class SpecialityUpdateView(UpdateView):
    model = Speciality
    form_class = SpecialityForm
    template_name = 'speciality_form.html'
    success_url = reverse_lazy('speciality_list')


class SpecialityDeleteView(DeleteView):
    model = Speciality
    template_name = 'speciality_confirm_delete.html'
    success_url = reverse_lazy('speciality_list')

