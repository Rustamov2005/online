from django.shortcuts import render, get_object_or_404, redirect
from .forms import CourseForm
from home.models import Courses


def curseviwe(request):
    return render(request, 'course.html')


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')  # 'course_list' - kurslar ro'yxati sahifasi
    else:
        form = CourseForm()
    return render(request, 'createcourse.html', {'form': form})


def delete_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')  # 'course_list' - kurslar ro'yxati sahifasi
    return render(request, 'courses/delete_course.html', {'course': course})


def update_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)  # 'course_detail' - kursning batafsil sahifasi
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/update_course.html', {'form': form})


