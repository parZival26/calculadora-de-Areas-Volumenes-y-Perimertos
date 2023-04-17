import unittest
import areas, perimetros, volumenes

class TestAreas(unittest.TestCase):
    def test_area_circulo(self):
        self.assertEqual(areas.area_of_circle(5), 78.54)
    
    def test_area_cuadrado(self):
        self.assertEqual(areas.area_of_square(5), 25)
    
    def test_area_rectangulo(self):
        self.assertEqual(areas.area_of_rectangle(5, 5), 25)
    
    def test_area_triangulo(self):
        self.assertEqual(areas.area_of_triangle(5, 5), 12.5)

class TestPerimetros(unittest.TestCase):
    def test_perimetro_circulo(self):
        self.assertEqual(perimetros.perimetro_circulo(5), 31.42)

    def test_perimetro_cuadrado(self):
        self.assertEqual(perimetros.perimetro_cuadrado(5), 20)
    
    def test_perimetro_rectangulo(self):
        self.assertEqual(perimetros.perimetro_rectangulo(5, 5), 20)
    
    def test_perimetro_triangulo(self):
        self.assertEqual(perimetros.perimetro_triangle(5, 5, 5), 15)

class TestVolumenes(unittest.TestCase):
    def test_volumen_esfera(self):
        self.assertEqual(volumenes.volumen_esfera(5), 523.6)
    
    def test_volumen_cubo(self):
        self.assertEqual(volumenes.volume_cube(5), 125)

    def test_volumen_cilindro(self):
        self.assertEqual(volumenes.volume_cylinder(5, 5), 392.7)