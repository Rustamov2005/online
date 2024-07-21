from django.shortcuts import render
from .models import Subjects, Courses, Teachers, Speciality


def spesialetyviwe(request):
    speciality = Speciality.objects.all()
    context = {'speciality': speciality}
    return render(request, 'index.html', context=context)


def home(request):
    teach = Teachers.objects.all()
    course = Courses.objects.all()
    subjects = Subjects.objects.all()
    return render(request, 'index.html', {'teachers': teach, 'course': course, 'subs': subjects})




