from django.test import TestCase
from ..juego.models import Juegos

class JuegoTestCase(TestCase):
 def setUp(self):
  a1 = Juegos.objects.create(titulo="Ejemplo",descripcion="Esta es una prueba",precio="12000",plataforma="Prueba",imagen="core/demon.jpg")
  Juegos.objects.create(titulo = "Harry Potter", autor = a1, resumen = "Resumen del libro")

 def test_juegos_titulo(self):
  juego1 = Juegos.objects.get(titulo="Ejemplo")
  self.assertEqual(juego1.titulo, "Esta es una prueba")  