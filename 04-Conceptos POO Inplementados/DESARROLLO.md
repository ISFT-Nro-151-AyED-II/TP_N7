# Resolución TP N°7 - Implementación de Conceptos POO Avanzados

## 💡 Enfoque técnico: Acoplamiento y Cohesión
* **Acoplamiento (Bajo):** Se logró un diseño de bajo acoplamiento aislando la capa de presentación (`Main.py`) de la capa de dominio (`JerarquiaAnimal.py`). La interfaz de consola no conoce los detalles internos de las subclases; se comunica con ellas puramente a través de los métodos públicos definidos en la clase base (`accionar_hablar`, `accionar_moverse`). Además, la instanciación dinámica usando un diccionario en lugar de sentencias condicionales duras previene el acoplamiento rígido del menú.
* **Cohesión (Fuerte vs Débil):** Se evitó deliberadamente la cohesión débil. Si las clases de los animales incluyeran sentencias `print()` o `input()`, estarían mezclando lógica de negocio con lógica de presentación. En cambio, se diseñó con **Cohesión Fuerte**: la clase `Animal` tiene una única macro-responsabilidad (gestionar el estado vital y orquestar comportamientos), y delega el I/O estrictamente al `Main.py`. El método `__consumir_energia()` es otro ejemplo de cohesión fuerte, ya que su única función matemática y algorítmica es calcular deducciones sobre el estado.

## 💡 Enfoque técnico: Encapsulamiento y Efecto Mariposa
* **Encapsulamiento:** Se profundizó la ocultación de información. No solo los atributos (`__nombre`, `__energia`) son privados mediante *name mangling*, sino que también se implementó comportamiento privado. El método `__consumir_energia()` es inaccesible desde el exterior. El sistema fuerza al usuario a interactuar mediante métodos públicos que gestionan el desgaste internamente.
* **Efecto Mariposa:** Para ilustrar este concepto arquitectónico (donde un pequeño cambio genera alteraciones masivas en todo el ecosistema de la aplicación), se definió la constante de clase `TASA_FATIGA_BASE = 5` en la superclase `Animal`. Si el día de mañana los requerimientos cambian y los animales deben cansarse más rápido, solo se modifica esa única línea en la clase base. Ese micro-cambio se propagará en cascada afectando el comportamiento de las instancias de Perro, Vaca y Abeja sin necesidad de modificar el código de sus respectivas clases.

## 💡 Enfoque técnico: Refactorización (Template Method)
Para unificar los conceptos anteriores de forma ordenada, se implementó el patrón de diseño *Template Method*. Los métodos públicos (`accionar_hablar()`) ahora funcionan como un "molde" que dicta los pasos invariables (validar energía disponible, descontar fatiga), y luego delegan la parte variable o polimórfica a métodos *protected* (`_emitir_sonido()`) que las subclases están obligadas a implementar.

---

## 💻 Simulación de Ejecución en Consola

```text
====================================
 SISTEMA DE GESTIÓN (CONCEPTOS POO)
====================================

1. Instanciar e interactuar (Prueba de Fatiga)
2. Inspeccionar metadatos de herencia
3. Salir

Elegí una opción: 1

Seleccioná el animal a instanciar:

1. Perro
2. Vaca
3. Abeja

Opción (1-3): 1

Ingresá un nombre para el animal: Albóndiga

✅ Objeto instanciado correctamente
====================================

Soy Albóndiga, clase Perro. Energía vital: 100%

[Acción 1]
Hablar: Guau!
Moverse: Caminando con 4 patas
> Energía restante: 85%

[Acción 2]
Hablar: Guau!
Moverse: Caminando con 4 patas
> Energía restante: 70%

[Acción 3]
Hablar: Guau!
Moverse: Caminando con 4 patas
> Energía restante: 55%

====================================
 SISTEMA DE GESTIÓN (CONCEPTOS POO)
====================================

1. Instanciar e interactuar (Prueba de Fatiga)
2. Inspeccionar metadatos de herencia
3. Salir

Elegí una opción: 3

Cerrando sistema.
