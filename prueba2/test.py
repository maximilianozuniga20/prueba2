import unittest
from django.test import TestCase
from juego.models import Juegos

class PRUEBAUNITARIA(unittest.TestCase):
    def test_crear_demo(self):
        a = 1
        self.assertEqual(a, 1)
    
    def test_crear_objeto(self):
        juego = Juegos.objects.create(titulo="Ejemplo",
                                      descripcion="Esta es una prueba",
                                      precio="12000",
                                      plataforma="Prueba",
                                      imagen="core/demon.jpg")
        juego.save()
        self.assertTrue(juego,True)

if __name__ == "__main__":
    unittest.main()

    

        
    
    

    


