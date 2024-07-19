from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from home.models import Teachers
from .forms import TeacherForm



def teacher(request):
    return render(request, 'teacher.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(" ")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'auth/login.html')


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"Password don't match!")
            return redirect('register')
    else:
        return render(request,"auth/regester.html")


def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # 'teacher_list' - o'qituvchilar ro'yxati sahifasi
    else:
        form = TeacherForm()
    return render(request, 'createteacher.html', {'form': form})


def update_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', pk=teacher.pk)  # 'teacher_detail' - o'qituvchining batafsil sahifasi
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'ubdateteacher.html', {'form': form})


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')  # 'teacher_list' - o'qituvchilar ro'yxati sahifasi
    return render(request, 'deleteteacher.html', {'teacher': teacher})



