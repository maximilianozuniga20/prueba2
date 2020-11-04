from django.test import TestCase
from principal.models import Libro, Autor

class LibroTestCase(TestCase):
 def setUp(self):
  a1 = Autor.objects.create(nombre="J.K. Rowling")
  a2 = Autor.objects.create(nombre="Miguel de Carvantes")
  Libro.objects.create(titulo = "Harry Potter", autor = a1, resumen = "Resumen del libro")
  Libro.objects.create(titulo = "El Quijote", autor = a2, resumen = "Resumen del libro")

 def test_libros_autor(self):
  libro1 = Libro.objects.get(titulo="Harry Potter")
  self.assertEqual(libro1.autor.nombre, "J.K. Rowling")  