# Resolución TP N°7 - Introducción a POO en Python

## 💡 Enfoque técnico: Creación de la clase e instanciación (Puntos 1.1 y 1.2)
Se optó por crear la clase `Calculadora` separando responsabilidades. En lugar de procesar los inputs (como `input()`) dentro de la clase, ésta solo recibe datos, los valida y devuelve resultados. Esto asegura alta cohesión y bajo acoplamiento. 
* **Atributo de clase (`total_operaciones_globales`):** Se definió para registrar un estado compartido. Si en el futuro el sistema requiere correr múltiples instancias concurrentes (ej. una calculadora por hilo/usuario), este atributo centraliza la estadística total sin recurrir a variables globales externas.
* **Atributos de instancia (`identificador_sesion`, `historial_local`):** Permiten que cada objeto mantenga su propio estado y trazabilidad, fundamental para evitar choques de información si el sistema escala.

## 💡 Enfoque técnico: Implementación de Métodos (Punto 1.3)
Se implementaron los tres tipos de métodos de Python según su función lógica:
* **Métodos de instancia (`sumar`, `restar`, etc.):** Alteran el estado de la instancia (guardando en el historial).
* **Método de clase (`obtener_estadisticas_globales`):** Decorado con `@classmethod`. Permite consultar métricas generales del sistema interactuando únicamente con el contexto de la clase, sin depender de objetos individuales.
* **Método estático (`validar_numero`):** Decorado con `@staticmethod`. La validación de un tipo de dato es un proceso puro (input -> output) que no requiere leer ni alterar el estado de la calculadora. Encapsularlo acá respeta el Principio de Responsabilidad Única.

## 💡 Enfoque técnico: Interfaz y Robustez (Punto 1.4)
Se diseñó un controlador CLI (`Main.py`) que consume la clase. Se aplicó programación defensiva estricta:
1.  Un ciclo de validación continuo en `solicitar_input_numerico` para asegurar que el sistema no colapse ante ingresos de *strings* o formatos vacíos.
2.  Manejo explícito de la excepción `ZeroDivisionError` a nivel de interfaz de usuario.
3.  Normalización de datos (conversión de coma a punto flotante) para adaptar el sistema a la tipografía regional del usuario, mejorando la usabilidad.

---

## 💻 Simulación de Ejecución en Consola

```text
Iniciando Sistema de Cálculo...

================
 MENÚ PRINCIPAL
================

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Ver estadísticas e historial
6. Salir

Seleccioná una operación (1-6): 1

Ingresá el primer valor: 10

Ingresá el segundo valor: quince

⚠️ Error de validación: El valor ingresado ('quince') no es numérico.. Reintentá.

Ingresá el segundo valor: 15

✅ Resultado exitoso: 25.0

================
 MENÚ PRINCIPAL
================

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Ver estadísticas e historial
6. Salir

Seleccioná una operación (1-6): 4

Ingresá el primer valor: 10

Ingresá el segundo valor: 0

❌ Error de ejecución: Error algorítmico: Intento de división por cero.

================
 MENÚ PRINCIPAL
================

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Ver estadísticas e historial
6. Salir

Seleccioná una operación (1-6): 5

HISTORIAL LOCAL (Sesión: Sesion_CLI_Principal)
===============================================

 - Suma: 10.0 + 15.0 = 25.0
> Total operaciones globales procesadas por la Clase: 1

================
 MENÚ PRINCIPAL
================

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Ver estadísticas e historial
6. Salir

Seleccioná una operación (1-6): 6

Cerrando sesión. Fin de la ejecución.