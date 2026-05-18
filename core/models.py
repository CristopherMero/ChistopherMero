from django.utils import timezone

from django.db import models

# Create your models here.



class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)


class Persona(models.Model):
    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    direction = models.CharField(max_length=100, verbose_name="Dirección")
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    titulo = models.CharField(max_length=100, verbose_name="Titulo Academico")
    biografia = models.TextField(max_length=1000, verbose_name="Biografia")
    correo = models.CharField(max_length=30, verbose_name="Correo Electronico")
    dedicacion = models.CharField(max_length=100, verbose_name="Dedicación Personal")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['-created']
        db_table = 'persona'

