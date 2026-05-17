from django.urls import path
from . import views

from django.conf.urls.static import static
from chistophermero import settings

urlpatterns = [
    path('portfolio', views.portfolio, name='portfolio')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)