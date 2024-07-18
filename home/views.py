from django.shortcuts import render
from .models import Subjects, Courses, Teachers, Speciality


def subjectsviwe(request):
    speciality = Speciality.objects.all()
    subjects = Subjects.objects.all()
    courses = Courses.objects.all()
    teachers = Teachers.objects.all()
    context = {
        'subjects': subjects,
        'speciality': speciality,
        'courses': courses,
        'teachers': teachers
    }
    return render(request, 'index.html', context)


def home(request):
    return render(request, 'index.html')




