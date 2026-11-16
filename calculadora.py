"""Interfaz de consola para la calculadora."""

import math

from operaciones import (
    division,
    factorial,
    modulo,
    multiplicacion,
    porcentaje,
    potencia,
    promedio,
    raiz_cuadrada,
    redondear,
    resta,
    suma,
    valor_absoluto,
)


class CalculadoraApp:
    """Administra el menú, las entradas y el historial de operaciones."""

    def __init__(self, input_fn=None, output_fn=None):
        self.input_fn = input if input_fn is None else input_fn
        self.output_fn = print if output_fn is None else output_fn
        self.historial = []

    def mostrar_menu(self):
        self.output_fn("\n========== CALCULADORA ==========")
        self.output_fn("1. Suma")
        self.output_fn("2. Resta")
        self.output_fn("3. Multiplicación")
        self.output_fn("4. División")
        self.output_fn("5. Módulo (residuo)")
        self.output_fn("6. Potencia")
        self.output_fn("7. Raíz cuadrada")
        self.output_fn("8. Porcentaje")
        self.output_fn("9. Valor absoluto")
        self.output_fn("10. Factorial")
        self.output_fn("11. Promedio")
        self.output_fn("12. Redondeo")
        self.output_fn("13. Mostrar historial")
        self.output_fn("14. Limpiar historial")
        self.output_fn("0. Salir")
        self.output_fn("================================")

    def _leer_opcion(self):
        while True:
            entrada = self.input_fn("Seleccione una opción: ")
            try:
                return int(entrada)
            except (TypeError, ValueError):
                self.output_fn("Entrada no válida. Seleccione una opción numérica.")

    def _leer_numero(self, mensaje, entero=False):
        while True:
            entrada = self.input_fn(mensaje)
            try:
                numero = float(entrada)
                if not math.isfinite(numero):
                    raise ValueError
                if entero:
                    if not numero.is_integer():
                        raise ValueError
                    return int(numero)
                return numero
            except (TypeError, ValueError):
                if entero:
                    self.output_fn("Entrada no válida. Introduzca un número entero.")
                else:
                    self.output_fn("Entrada no válida. Introduzca un número.")

    def _guardar_resultado(self, expresion, resultado):
        registro = f"{expresion} = {resultado}"
        self.historial.append(registro)
        self.output_fn(f"Resultado: {resultado}")

    def mostrar_historial(self):
        if not self.historial:
            self.output_fn("El historial está vacío.")
            return
        self.output_fn("Historial de operaciones:")
        for indice, operacion in enumerate(self.historial, start=1):
            self.output_fn(f"{indice}. {operacion}")

    def limpiar_historial(self):
        self.historial.clear()
        self.output_fn("El historial fue limpiado.")

    def realizar_operacion(self, opcion):
        if opcion in (1, 2, 3, 4, 5, 6):
            a = self._leer_numero("Ingrese el primer número: ")
            b = self._leer_numero("Ingrese el segundo número: ")
            operaciones = {
                1: (suma, "+"),
                2: (resta, "-"),
                3: (multiplicacion, "*"),
                4: (division, "/"),
                5: (modulo, "%"),
                6: (potencia, "**"),
            }
            funcion, simbolo = operaciones[opcion]
            resultado = funcion(a, b)
            self._guardar_resultado(f"{a} {simbolo} {b}", resultado)
            return

        if opcion in (7, 9, 10):
            if opcion == 10:
                numero = self._leer_numero("Ingrese un número entero: ", entero=True)
                resultado = factorial(numero)
                expresion = f"{numero}!"
            else:
                numero = self._leer_numero("Ingrese un número: ")
                if opcion == 7:
                    resultado = raiz_cuadrada(numero)
                    expresion = f"raíz cuadrada de {numero}"
                else:
                    resultado = valor_absoluto(numero)
                    expresion = f"|{numero}|"
            self._guardar_resultado(expresion, resultado)
            return

        if opcion == 8:
            cantidad = self._leer_numero("Ingrese la cantidad: ")
            porcentaje_ingresado = self._leer_numero("Ingrese el porcentaje: ")
            resultado = porcentaje(cantidad, porcentaje_ingresado)
            self._guardar_resultado(
                f"{porcentaje_ingresado}% de {cantidad}", resultado
            )
            return

        if opcion == 11:
            cantidad = self._leer_numero(
                "¿Cuántos números desea promediar?: ", entero=True
            )
            if cantidad <= 0:
                raise ValueError("Debe ingresar una cantidad mayor que cero.")
            numeros = [
                self._leer_numero(f"Ingrese el número {indice}: ")
                for indice in range(1, cantidad + 1)
            ]
            resultado = promedio(*numeros)
            self._guardar_resultado(f"promedio de {numeros}", resultado)
            return

        if opcion == 12:
            numero = self._leer_numero("Ingrese el número: ")
            decimales = self._leer_numero(
                "Ingrese la cantidad de decimales: ", entero=True
            )
            resultado = redondear(numero, decimales)
            self._guardar_resultado(
                f"redondear {numero} a {decimales} decimales", resultado
            )

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = self._leer_opcion()

            if opcion == 0:
                self.output_fn("Calculadora finalizada.")
                break
            if opcion == 13:
                self.mostrar_historial()
                continue
            if opcion == 14:
                self.limpiar_historial()
                continue
            if 1 <= opcion <= 12:
                try:
                    self.realizar_operacion(opcion)
                except ValueError as error:
                    self.output_fn(f"Error: {error}")
                continue
            self.output_fn("Opción no válida. Seleccione una opción del menú.")


if __name__ == "__main__":
    CalculadoraApp().ejecutar()
