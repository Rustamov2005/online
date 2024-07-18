from django.urls import path
from .views import blog, commints, categories, blogdetailviwe


urlpatterns = [
    path('blogdetail/', blog, name='blog'),
    path('commints/', commints, name='commints'),
    path('categories/', categories, name='categories'),
    path('blogdetailviwe/', blogdetailviwe, name='blogdetailviwe'),
]
