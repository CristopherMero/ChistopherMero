from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from .models import Persona

from core.models import ToDoItem


class AllToDos(ListView):
    model = ToDoItem
    template_name = "core/index.html"

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    persona = Persona.objects.all()
    return render(request, 'core/contact.html', {
        'personas': persona
    })


def about(request):
    return render(request, 'core/about.html')