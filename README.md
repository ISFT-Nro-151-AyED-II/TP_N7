# 🐍 Trabajo Práctico N°2 - Tercera Parte

**Instituto Superior de Formación Técnica Nº 151**  
**Carrera:** Tecnicatura Superior en Análisis de Sistemas   
**Materia:** Algoritmos y Estructuras de Datos II  
**Tema:** Paradigma de Programación Orientada a Objetos (POO) en Python  
**Alumno:** David Hernán Bravo

---

## 🎯 Objetivo del Repositorio
Este repositorio contiene la resolución del marco práctico sobre POO en Python. El diseño de las soluciones se enfocó en la escalabilidad, la alta cohesión, el bajo acoplamiento y la programación defensiva, separando estrictamente la lógica de dominio (modelos/clases) de la interfaz de usuario (controladores CLI).

A continuación, se detalla el índice de las implementaciones con sus respectivos análisis técnicos.

---

## 📂 Índice de Implementaciones y Desarrollo

### 🧮 1. Introducción a POO (Calculadora)
Implementación de una clase base aislada de la interfaz I/O. Se aplican métodos de instancia, de clase (`@classmethod` para métricas globales) y estáticos (`@staticmethod` para validación pura de tipos de datos).
* 📄 **Documentación y Arquitectura:** [Ver DESARROLLO.md](./1-Introducción%20a%20POO/DESARROLLO.md)

### 🧬 2. Herencia (Jerarquía Animal)
Diseño de una superclase `Animal` que delega comportamiento mediante polimorfismo, forzando la implementación de métodos en sus subclases (`Perro`, `Vaca`, `Abeja`). Incluye introspección del árbol de herencia usando `__bases__` y `__subclasses__()`.
* 📄 **Documentación y Arquitectura:** [Ver DESARROLLO.md](./2-Herencia/DESARROLLO.md)

### 🔒 3. Decoradores y Encapsulamiento
Refactorización del modelo de dominio animal aplicando encapsulamiento estricto mediante *name mangling* (`__`). Exposición controlada del estado interno mediante decoradores `@property` (Getters) y validación de reglas de negocio en `@setter`.
* 📄 **Documentación y Arquitectura:** [Ver DESARROLLO.md](./03-Decoradores/DESARROLLO.md)

### 🧩 4. Conceptos POO Implementados Avanzados
Elevación del nivel arquitectónico implementando el patrón *Template Method*. Se demuestra el **Efecto Mariposa** mediante constantes de clase centralizadas, y se asegura un entorno de **Alta Cohesión** y **Bajo Acoplamiento** delegando el cálculo de fatiga a métodos privados.
* 📄 **Documentación y Arquitectura:** [Ver DESARROLLO.md](./04-Conceptos%20POO%20Implementados/DESARROLLO.md)

### 🔄 5. Polimorfismo
Análisis del *Duck Typing* nativo de Python en un ciclo `for`. Se implementa una capa de seguridad algorítmica validando contratos (`isinstance`) para evitar caídas de sistema (AttributeError) ante la inyección de objetos anómalos.
* 📄 **Documentación y Arquitectura:** [Ver DESARROLLO.md](./05-Polimorfismo/DESARROLLO.md)

### 🚁 6. Clases Abstractas e Interfaces
Implementación del Principio de Inversión de Dependencias (SOLID). Creación de una interfaz estricta `IPilotable` usando el módulo `abc` para el control de múltiples drones. Se centraliza la máquina de estados en una clase abstracta `DronBase` para respetar el principio DRY.
* 📄 **Documentación y Arquitectura:** [Ver DESARROLLO.md](./06-Clases%20Abstractas%20e%20Interfaces/DESARROLLO.md)

### 🦆 7. Duck Typing
Demostración del paso de mensajes dinámico. En lugar de forzar contratos formales, se procesa un lote de entidades evaluando sus capacidades en tiempo de ejecución (introspección con `hasattr()`). Se prioriza el paradigma defensivo LBYL (*Look Before You Leap*).
* 📄 **Documentación y Arquitectura:** [Ver DESARROLLO.md](./07-Duck%20Typing/DESARROLLO.md)

---
*Repositorio mantenido y estructurado para la cátedra de Algoritmos y Estructuras de Datos II.*
