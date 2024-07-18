from django.contrib import admin
from .models import Subjects, Courses, Teachers, Speciality

admin.site.register(Subjects)
admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(Speciality)
