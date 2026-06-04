# Resolución TP N°7 - Análisis de Polimorfismo en Python

## 💡 Enfoque técnico: Polimorfismo, Duck Typing y Contratos Estrictos
El fragmento de código base analizado (`for animal in Perro(), Gato(): animal.hablar()`) demuestra el soporte nativo de Python para polimorfismo ad-hoc. En Python, las variables no tienen tipo estático, los objetos sí. Por lo tanto, el ciclo `for` simplemente envía el mensaje `hablar()` a cualquier objeto que atraviese en la iteración. A esto se lo denomina **Duck Typing**. 

**Decisión arquitectónica:** En sistemas grandes y escalables, el Duck Typing indiscriminado genera vulnerabilidades críticas. Si la colección de objetos recibe datos dinámicos (por ejemplo, desde una API o una base de datos) y se introduce una instancia sin el método `hablar()`, el ciclo se interrumpe abruptamente con un `AttributeError`. Para solucionar esto, se implementaron dos capas de protección en la arquitectura:
1.  **Clase Base Abstracta (`Animal`):** Se definió un contrato superior que obliga a cualquier subclase a tener implementado el método `hablar()`.
2.  **Validación de Tipo (`isinstance`):** Antes de enviar el mensaje polimórfico en el iterador, el algoritmo valida que la instancia pertenezca a la familia `Animal`. Esto transforma un posible fallo crítico en tiempo de ejecución en una excepción controlada (`TypeError`), permitiendo que el bucle de procesamiento continúe operando con el resto de los objetos válidos.

---

## 💻 Simulación de Ejecución en Consola

Para probar la robustez del código, se introdujo intencionalmente un objeto de tipo `Dron` (que no hereda de `Animal` ni tiene el método `hablar()`) dentro de la tupla original de perros y gatos.

```text

=======================
 EJECUCIÓN POLIMÓRFICA
=======================

> [Perro] emitió el sonido: Guau!
> [Gato] emitió el sonido: Miau!
❌ Error de Integridad: Inconsistencia: El objeto de clase 'Dron' no respeta el contrato 'Animal'.