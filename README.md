# Ampliación de la calculadora

**Práctica 2:** ampliación de una calculadora en Python utilizando Git, GitHub Issues y Markdown.

## Descripción

Aplicación de consola desarrollada en Python que permite realizar operaciones matemáticas, validar los datos ingresados y consultar o limpiar el historial de operaciones durante la ejecución.

## Funcionalidades y estado

| N.º | Funcionalidad | Estado |
|---:|---|---|
| 1 | Potencia: elevar una base a un exponente positivo, negativo o cero. | Implementada |
| 2 | Módulo: obtener el residuo de una división. | Implementada |
| 3 | Raíz cuadrada: calcular la raíz y rechazar números negativos. | Implementada |
| 4 | Porcentaje: calcular un porcentaje de una cantidad. | Implementada |
| 5 | Valor absoluto: obtener el valor absoluto de un número. | Implementada |
| 6 | Factorial: calcular el factorial de un entero no negativo. | Implementada |
| 7 | Promedio: calcular el promedio de varios números. | Implementada |
| 8 | Redondeo: redondear un resultado a los decimales indicados. | Implementada |
| 9 | Validación de entradas: controlar datos no numéricos y valores no finitos. | Implementada |
| 10 | División por cero: evitar división y módulo con divisor cero. | Implementada |
| 11 | Menú: organizar las operaciones en opciones claras. | Implementada |
| 12 | Repetición: permitir realizar varias operaciones sin reiniciar el programa. | Implementada |
| Adicional 1 | Historial: almacenar y mostrar las operaciones de la sesión. | Implementada |
| Adicional 2 | Limpiar historial: borrar los registros de la sesión. | Implementada |
| Adicional 3 | Documentación: incluir descripción, tabla, instalación y ejemplos. | Implementada |
| Base | Suma, resta, multiplicación y división. | Implementadas |

## Estructura del proyecto

El proyecto contiene dos archivos Python, respetando el máximo establecido en la práctica:

```text
ampliacion-calculadora/
├── README.md
├── calculadora.py
└── operaciones.py
```

- **calculadora.py:** muestra el menú, solicita los datos, valida las entradas, presenta los resultados y controla la repetición y el historial.
- **operaciones.py:** contiene las funciones matemáticas y realiza los cálculos.

## Tecnologías utilizadas

- Python 3.10 o superior.
- Git para el control de versiones.
- GitHub para alojar el repositorio y organizar las tareas mediante Issues.
- Markdown para la documentación.

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
   python calculadora.py
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

## Autor

**Carlos Ailton Villca Alcocer**

Usuario de GitHub: `villca06carlos24-a11y`
