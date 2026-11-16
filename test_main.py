"""Pruebas de la interfaz de consola."""

import unittest

from main import CalculadoraApp


class TestCalculadoraApp(unittest.TestCase):
    def crear_app(self, entradas):
        iterador = iter(entradas)
        salidas = []
        app = CalculadoraApp(
            input_fn=lambda _mensaje: next(iterador),
            output_fn=salidas.append,
        )
        return app, salidas

    def test_repite_operaciones_y_permite_salir(self):
        app, salidas = self.crear_app(["1", "2", "3", "4", "10", "2", "0"])
        app.ejecutar()
        self.assertEqual(len(app.historial), 2)
        self.assertIn("2.0 + 3.0 = 5.0", app.historial)
        self.assertIn("10.0 / 2.0 = 5.0", app.historial)
        self.assertIn("Calculadora finalizada.", salidas)

    def test_entrada_no_numerica_no_cierra_programa(self):
        app, salidas = self.crear_app(["1", "abc", "2", "3", "0"])
        app.ejecutar()
        self.assertEqual(len(app.historial), 1)
        self.assertTrue(any("Entrada no válida" in texto for texto in salidas))

    def test_historial_y_limpieza(self):
        app, salidas = self.crear_app(["1", "2", "3", "13", "14", "13", "0"])
        app.ejecutar()
        self.assertEqual(app.historial, [])
        self.assertTrue(any("Historial de operaciones:" in texto for texto in salidas))
        self.assertTrue(any("El historial fue limpiado." in texto for texto in salidas))
        self.assertTrue(any("El historial está vacío." in texto for texto in salidas))

    def test_division_por_cero_no_registra_operacion(self):
        app, salidas = self.crear_app(["4", "10", "0", "0"])
        app.ejecutar()
        self.assertEqual(app.historial, [])
        self.assertTrue(any("No se puede dividir entre cero." in texto for texto in salidas))


if __name__ == "__main__":
    unittest.main()
