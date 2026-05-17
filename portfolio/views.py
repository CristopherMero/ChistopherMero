from django.shortcuts import render
from .models import proyectos
# Create your views here.


def portfolio(request):

    proyecto = proyectos.objects.all()
    return render(request, 'core/portfolio.html', {
        'proyectos': proyecto
    })