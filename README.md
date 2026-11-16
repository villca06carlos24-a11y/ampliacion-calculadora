# ampliacion-calculadora

Práctica 2- Ampliación de calculadora en Python con Git y GitHub Issues.

## Descripción

Aplicación de consola desarrollada en Python que permite realizar operaciones aritméticas y matemáticas, validar los datos ingresados y consultar o limpiar el historial de operaciones durante la ejecución.

## Operaciones y estado

| Operación | Descripción | Estado |
|---|---|---|
| Suma | Suma dos números. | Implementada |
| Resta | Resta dos números. | Implementada |
| Multiplicación | Multiplica dos números. | Implementada |
| División | Divide dos números y evita la división entre cero. | Implementada |
| Módulo | Obtiene el residuo de una división y valida el divisor. | Implementada |
| Potencia | Eleva una base a un exponente positivo, negativo o cero. | Implementada |
| Raíz cuadrada | Calcula la raíz cuadrada y rechaza números negativos. | Implementada |
| Porcentaje | Calcula un porcentaje de una cantidad. | Implementada |
| Valor absoluto | Devuelve el valor absoluto de un número. | Implementada |
| Factorial | Calcula el factorial de un entero no negativo. | Implementada |
| Promedio | Calcula el promedio de varios números. | Implementada |
| Redondeo | Redondea un número a la cantidad de decimales indicada. | Implementada |
| Historial | Registra y muestra las operaciones de la sesión. | Implementada |
| Limpiar historial | Elimina los registros de la sesión. | Implementada |

## Tecnologías utilizadas

- Python 3.10 o superior.
- Módulo `unittest` de la biblioteca estándar para las pruebas.
- Git y GitHub para el control de versiones y seguimiento del trabajo.

## Instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/villca06carlos24-a11y/ampliacion-calculadora.git
   ```

2. Entrar en la carpeta del proyecto:

   ```bash
   cd ampliacion-calculadora
   ```

3. Verificar que Python esté instalado:

   ```bash
   python --version
   ```

4. Ejecutar la calculadora:

   ```bash
   python main.py
   ```

No se necesitan instalar dependencias externas.

## Ejemplos de uso

Al iniciar el programa se muestra un menú con las operaciones disponibles.

- **Porcentaje:** seleccionar la opción 8, ingresar la cantidad `200` y el porcentaje `15`. El resultado será `30.0`.
- **Potencia:** seleccionar la opción 6, ingresar la base `2` y el exponente `3`. El resultado será `8.0`.
- **Módulo:** seleccionar la opción 5, ingresar `10` y `3`. El residuo será `1.0`.
- **Promedio:** seleccionar la opción 11, indicar cuántos números se promediarán e introducir cada valor.
- **Historial:** seleccionar la opción 13 para consultar las operaciones realizadas.
- **Limpiar historial:** seleccionar la opción 14 para borrar los registros de la sesión.
- **Salir:** seleccionar la opción 0 para finalizar el programa.

Las entradas no numéricas se vuelven a solicitar. Las operaciones no permitidas, como dividir entre cero o calcular la raíz cuadrada de un número negativo, muestran un mensaje de error sin cerrar la aplicación.

## Ejecución de pruebas

Para ejecutar todas las pruebas unitarias desde la carpeta del proyecto:

```bash
python -m unittest discover -v
```

Las pruebas verifican las operaciones matemáticas, los casos límite, las validaciones, el menú, la repetición de operaciones y el historial.

## Autor

- Nombre completo del autor: **Pendiente de confirmar**.
- Usuario de GitHub: `villca06carlos24-a11y`.
