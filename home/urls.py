from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import  spesialetyviwe

urlpatterns = [
                  path('home/', home, name='home'),
                  path('home/spesiaietyviwe/', spesialetyviwe, name='spesiaietyviwe'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
