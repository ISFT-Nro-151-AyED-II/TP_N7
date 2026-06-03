# Resolución TP N°7 - Decoradores y Encapsulamiento en Python

## 💡 Enfoque técnico: Encapsulamiento (Punto 3.2)
Se aplicó encapsulamiento estricto en la clase `Animal` utilizando el *name mangling* de Python (prefijo `__` en los atributos `__nombre` y `__energia`). Esta decisión arquitectónica protege el estado interno de los objetos. En un sistema escalable, acceder directamente a un atributo (ej. `objeto.energia = 999`) viola el encapsulamiento y permite la corrupción de los datos. Al usar variables privadas, forzamos a que cualquier alteración del estado deba pasar por una interfaz controlada.

## 💡 Enfoque técnico: Decoradores @property y Setters (Puntos 3.1 y 3.3)
Para exponer los atributos encapsulados sin romper el contrato de la clase, se utilizaron decoradores:
* **`@property` (Getters):** Permite que el controlador (`Main.py`) lea el valor de `__nombre` y `__energia` como si fueran atributos públicos (ej. `instancia.energia`), manteniendo la sintaxis limpia pero ejecutando un método subyacente.
* **`@setter` (Setters):** Se delegó la responsabilidad de validar las reglas de negocio al propio modelo de dominio. El setter de `energia`, por ejemplo, impide activamente que se asigne un valor fuera del rango `0-100` lanzando un `ValueError`. Esto garantiza una alta cohesión: la clase `Animal` es la única responsable de saber qué constituye un dato válido para sí misma.

---

## 💻 Simulación de Ejecución en Consola

```text

================================
 SISTEMA DE GESTIÓN DE HERENCIA
================================

1. Instanciar e interactuar con animales.
2. Inspeccionar metadatos de herencia.
3. Salir

Elegí una opción del menú: 1

Seleccioná el animal a instanciar:

1. Perro
2. Vaca
3. Abeja

Opción (1-3): 1

Ingresá un nombre para el animal: Rabito

✅ Objeto instanciado correctamente.

Describirme: Soy Rabito, un objeto de la clase Perro.
Hablar: Guau!
Moverse: Caminando con 4 patas

[Prueba de Property] Energía actual de Rabito: 100%

Ingresá nueva energía para Rabito (0-100) para probar el Setter: 150

❌ Error durante la interacción: Regla de negocio vulnerada: La energía debe estar entre 0 y 100.

================================
 SISTEMA DE GESTIÓN DE HERENCIA
================================

1. Instanciar e interactuar con animales.
2. Inspeccionar metadatos de herencia.
3. Salir

Elegí una opción del menú: 1

Seleccioná el animal a instanciar:

1. Perro
2. Vaca
3. Abeja

Opción (1-3): 1

Ingresá un nombre para el animal: Albóndiga

✅ Objeto instanciado correctamente.

Describirme: Soy Albóndiga, un objeto de la clase Perro.
Hablar: Guau!
Moverse: Caminando con 4 patas

[Prueba de Property] Energía actual de Albóndiga: 100%

Ingresá nueva energía para Albóndiga (0-100) para probar el Setter: 85

✅ [Prueba de Setter exitosa] Nueva energía registrada: 85%

================================
 SISTEMA DE GESTIÓN DE HERENCIA
================================

1. Instanciar e interactuar con animales.
2. Inspeccionar metadatos de herencia.
3. Salir

Elegí una opción del menú: 3

Cerrando sistema.