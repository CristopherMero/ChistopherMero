from sys import path

from django.conf.urls.static import static
from django.urls import path

from chistophermero import settings
from . import views

urlpatterns = [
    path('', views.AllToDos.as_view(), name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)