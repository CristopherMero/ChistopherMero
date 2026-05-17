from django.utils import timezone

from django.db import models

# Create your models here.



class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)


