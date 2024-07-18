from django.urls import path
from .views import contact


urlpatterns = [
    path('contsct/', contact, name='contact'),
]