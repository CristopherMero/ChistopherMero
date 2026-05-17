from django.shortcuts import render

from .models import personas


# Create your views here.


def contact(request):
    persona = personas.objects.all()
    return render(request, 'core/contact.html', {
        'personas': persona
    })
