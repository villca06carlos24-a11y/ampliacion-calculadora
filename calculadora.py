"""Operaciones de la calculadora."""


def potencia(base: int | float, exponente: int | float) -> int | float:
    """Calcula la potencia de una base elevada a un exponente.

    Admite exponentes positivos, negativos y cero.
    """
    if base == 0 and exponente < 0:
        raise ValueError(
            "No se puede elevar cero a un exponente negativo."
        )

    return base ** exponente
