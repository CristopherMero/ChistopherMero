from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from core.models import ToDoItem


class AllToDos(ListView):
    model = ToDoItem
    template_name = "core/index.html"

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')