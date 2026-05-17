from django.db import models

# Create your models here.

from django.db import models

class proyectos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to='projects/', null=True, blank=True)
    enlace = models.URLField(null=True, blank=True)
    author = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created']
        db_table = 'proyectos'