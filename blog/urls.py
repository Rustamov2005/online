from django.urls import path
from .views import blog, commints, blogdetailviwe, create_blog, update_blog, delete_blog


urlpatterns = [
    path('blogdetail/', blog, name='blog'),
    path('commints/', commints, name='commints'),
    path('blogdetailviwe/', blogdetailviwe, name='blogdetailviwe'),
    path('blog/create/', create_blog, name='create_blog'),
    path('blog/<int:pk>/update/', update_blog, name='update_blog'),
    path('blog/<int:pk>/delete/', delete_blog, name='delete_blog'),
]
