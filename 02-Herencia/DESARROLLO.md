# Resolución TP N°7 - Herencia en Python

## 💡 Enfoque técnico: Creación de estructura y herencia (Puntos 2.1 y 2.2)
La arquitectura se divide en dos capas: modelo de dominio (`JerarquiaAnimal.py`) y presentador/controlador CLI (`Main.py`). 
En la clase base `Animal`, los métodos `hablar()` y `moverse()` lanzan una excepción `NotImplementedError`. Esta decisión de diseño se toma porque `Animal` actúa conceptualmente como una clase abstracta o interfaz. Forzamos a que cualquier desarrollador que herede de `Animal` esté obligado a sobrescribir esos métodos (polimorfismo), garantizando que no existan animales genéricos con comportamientos indefinidos en memoria. El método `describirme()` aprovecha la introspección (`type(self).__name__`) para resolver su identidad dinámicamente desde la clase base, evitando replicar código inútil en cada subclase.

## 💡 Enfoque técnico: Introspección y Metadatos (Puntos 2.3 y 2.4)
Python provee herramientas *built-in* para evaluar el árbol de herencia en tiempo de ejecución:
* **`__bases__`**: Es un atributo de la clase (no del objeto) que devuelve una tupla con todas las clases de las cuales hereda directamente. Es fundamental en casos de herencia múltiple para entender la jerarquía (MRO).
* **`__subclasses__()`**: Es un método que rastrea la memoria y devuelve una lista de las referencias a todas las clases que heredan de la actual. Se implementó mediante una *list comprehension* para formatear la salida y mostrar solo los nombres por consola.
* **Implementación de `base()`**: En Python no existe una función nativa llamada `base()`. Desde el punto de vista algorítmico, el acceso a la superclase principal se realiza a través del atributo escalar `__base__` (a diferencia de `__bases__` que es una tupla) o mediante el uso de `super()`. En el código se optó por demostrar la introspección con `__base__` para mantener la coherencia con el pedido de evaluar metadatos.

## 💡 Enfoque técnico: Instanciación e Interacción (Punto 2.5)
Para interactuar con el usuario, en lugar de usar un bloque rígido de `if/elif/else`, se implementó un "Factory Registry" (un diccionario que mapea strings a referencias de clase). Esto mejora drásticamente la escalabilidad algorítmica (Big O(1) de acceso) y permite añadir nuevas subclases en el futuro modificando una sola estructura de datos, respetando el principio Abierto/Cerrado (Open/Closed Principle) de SOLID. Todo el proceso está cubierto por bloques `try...except` para evitar la caída del sistema ante *inputs* erróneos.

---

## 💻 Simulación de Ejecución en Consola

```text

================================
 SISTEMA DE GESTIÓN DE HERENCIA
================================

1. Instanciar e interactuar con animales (Punto 2.5)
2. Inspeccionar metadatos de herencia (Puntos 2.3 y 2.4)
3. Salir

Elegí una opción del menú: 1

Seleccioná el animal a instanciar:

1. Perro
2. Vaca
3. Abeja

Opción (1-3): 5

❌ Error durante la instanciación:
La opción seleccionada no corresponde a un animal válido.

================================
 SISTEMA DE GESTIÓN DE HERENCIA
================================

1. Instanciar e interactuar con animales (Punto 2.5)
2. Inspeccionar metadatos de herencia (Puntos 2.3 y 2.4)
3. Salir

Elegí una opción del menú: 1

Seleccioná el animal a instanciar:

1. Perro
2. Vaca
3. Abeja

Opción (1-3): 3
✅ Objeto instanciado correctamente.

Describirme: Soy un objeto de la clase Abeja.
Hablar: Bzzzz!
Moverse: Volando

================================
 SISTEMA DE GESTIÓN DE HERENCIA
================================

1. Instanciar e interactuar con animales (Punto 2.5)
2. Inspeccionar metadatos de herencia (Puntos 2.3 y 2.4)
3. Salir

Elegí una opción del menú: 2

 METADATOS E INTROSPECCIÓN DE CLASES
=====================================

> Tupla __bases__ de Perro: (<class 'JerarquiaAnimal.Animal'>,)
> Subclases de Animal: ['Perro', 'Vaca', 'Abeja']
> Atributo __base__ de Vaca: <class 'JerarquiaAnimal.Animal'>

================================
 SISTEMA DE GESTIÓN DE HERENCIA
================================

1. Instanciar e interactuar con animales (Punto 2.5)
2. Inspeccionar metadatos de herencia (Puntos 2.3 y 2.4)
3. Salir

Elegí una opción del menú: 3

Cerrando sistema.