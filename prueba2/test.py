from django.test import TestCase
from .models import Juegos

class LibroTestCase(TestCase):
 def setUp(self):
  a1 = Juegos.objects.create(titulo="Ejemplo",descripcion="Esta es una prueba",precio="12000",plataforma="Prueba",imagen="core/demon.jpg")
  Juegos.objects.create(titulo = "Harry Potter", autor = a1, resumen = "Resumen del libro")

 def test_libros_autor(self):
  juego1 = Juegos.objects.get(titulo="Ejemplo")
  self.assertEqual(juego1.autor.titulo, "Esta es una prueba")  