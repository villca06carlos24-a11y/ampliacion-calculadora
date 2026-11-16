"""Funciones matemáticas de la calculadora."""


def suma(a: int | float, b: int | float) -> int | float:
    return a + b


def resta(a: int | float, b: int | float) -> int | float:
    return a - b


def multiplicacion(a: int | float, b: int | float) -> int | float:
    return a * b


def division(dividendo: int | float, divisor: int | float) -> int | float:
    if divisor == 0:
        raise ValueError("No se puede dividir entre cero.")
    return dividendo / divisor


def modulo(dividendo: int | float, divisor: int | float) -> int | float:
    if divisor == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero.")
    return dividendo % divisor


def potencia(base: int | float, exponente: int | float) -> int | float:
    """Calcula una potencia con exponentes positivos, negativos o cero."""
    if base == 0 and exponente < 0:
        raise ValueError("No se puede elevar cero a un exponente negativo.")
    return base ** exponente


def raiz_cuadrada(numero: int | float) -> float:
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return numero ** 0.5


def porcentaje(cantidad: int | float, porcentaje: int | float) -> int | float:
    return cantidad * porcentaje / 100


def valor_absoluto(numero: int | float) -> int | float:
    return abs(numero)


def factorial(numero: int) -> int:
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise ValueError("El factorial solo acepta números enteros.")
    if numero < 0:
        raise ValueError("El factorial no acepta números negativos.")
    resultado = 1
    for valor in range(2, numero + 1):
        resultado *= valor
    return resultado


def promedio(*numeros: int | float) -> float:
    if not numeros:
        raise ValueError("Debe ingresar al menos un número para calcular el promedio.")
    return sum(numeros) / len(numeros)


def redondear(numero: int | float, decimales: int = 0) -> int | float:
    if isinstance(decimales, bool) or not isinstance(decimales, int):
        raise ValueError("La cantidad de decimales debe ser un número entero.")
    if decimales < 0:
        raise ValueError("La cantidad de decimales no puede ser negativa.")
    return round(numero, decimales)
