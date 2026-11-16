"""Pruebas unitarias de las funciones matemáticas."""

import unittest

from calculadora import (
    division, factorial, modulo, multiplicacion, porcentaje, potencia,
    promedio, raiz_cuadrada, redondear, resta, suma, valor_absoluto,
)


class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(7, 4), 3)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 4), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            division(10, 0)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_por_cero(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_potencia_positiva(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_potencia_negativa(self):
        self.assertEqual(potencia(2, -2), 0.25)

    def test_potencia_cero(self):
        self.assertEqual(potencia(5, 0), 1)

    def test_cero_con_exponente_negativo(self):
        with self.assertRaises(ValueError):
            potencia(0, -2)

    def test_raiz_cuadrada_exacta(self):
        self.assertEqual(raiz_cuadrada(81), 9)

    def test_raiz_cuadrada_no_exacta(self):
        self.assertAlmostEqual(raiz_cuadrada(2), 2 ** 0.5)

    def test_raiz_negativa(self):
        with self.assertRaises(ValueError):
            raiz_cuadrada(-4)

    def test_porcentaje(self):
        self.assertEqual(porcentaje(200, 15), 30)

    def test_valor_absoluto(self):
        self.assertEqual(valor_absoluto(-8), 8)
        self.assertEqual(valor_absoluto(8), 8)
        self.assertEqual(valor_absoluto(0), 0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            factorial(-3)

    def test_factorial_no_entero(self):
        with self.assertRaises(ValueError):
            factorial(2.5)

    def test_promedio(self):
        self.assertEqual(promedio(2, 4, 6), 4)

    def test_promedio_sin_datos(self):
        with self.assertRaises(ValueError):
            promedio()

    def test_redondeo(self):
        self.assertEqual(redondear(3.14159, 2), 3.14)
        self.assertEqual(redondear(3.14159, 3), 3.142)

    def test_redondeo_decimales_invalidos(self):
        with self.assertRaises(ValueError):
            redondear(3.14, -1)


if __name__ == "__main__":
    unittest.main()
