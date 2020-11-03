from django.db import models

# Create your models here.
class Juegos(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length = 200)
    descripcion = models.CharField(verbose_name="Descripción", max_length = 250)
    precio = models.IntegerField(verbose_name="Precio", default=0)
    plataforma = models.CharField(verbose_name="Plataforma", max_length = 100)
    imagen = models.ImageField(upload_to = 'productos', null = True, blank = True)

    def __str__(self):
        return self.titulo