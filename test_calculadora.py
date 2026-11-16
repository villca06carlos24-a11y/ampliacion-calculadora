"""Pruebas unitarias para las operaciones de la calculadora."""

import unittest

from calculadora import potencia


class TestPotencia(unittest.TestCase):
    def test_exponente_positivo(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_exponente_negativo(self):
        self.assertEqual(potencia(2, -2), 0.25)

    def test_exponente_cero(self):
        self.assertEqual(potencia(5, 0), 1)

    def test_base_cero_con_exponente_positivo(self):
        self.assertEqual(potencia(0, 4), 0)

    def test_base_cero_con_exponente_negativo(self):
        with self.assertRaises(ValueError):
            potencia(0, -2)


if __name__ == "__main__":
    unittest.main()
