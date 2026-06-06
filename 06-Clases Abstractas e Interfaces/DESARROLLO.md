# Resolución TP N°7 - Clases Abstractas e Interfaces

## 💡 Enfoque técnico: Interfaz Estricta (`IPilotable`)
Se implementó una arquitectura basada en el Principio de Inversión de Dependencias (SOLID). Se definió un contrato puro (`IPilotable`) utilizando la librería `abc` de Python. Esta decisión arquitectónica fuerza a que cualquier entidad que desee ser operada por el sistema cliente tenga que implementar obligatoriamente los 6 métodos solicitados. Esto anula el riesgo de fallos en tiempo de ejecución por métodos faltantes en futuras integraciones de nuevos drones.

## 💡 Enfoque técnico: Centralización de Estados (`DronBase`)
En lugar de replicar el código de validación de despegue y aterrizaje en las 5 clases de drones, se creó una clase abstracta de conveniencia (`DronBase`) que hereda de la interfaz e implementa las reglas de la física (ej. "no podés acelerar si no despegaste"). Las clases concretas (`Tricoptero`, `Cuadricoptero`, etc.) simplemente heredan esta lógica base inyectando sus propiedades únicas (nombre y número de rotores). Esto garantiza el principio DRY (Don't Repeat Yourself) y asegura una mantenibilidad escalable.

## 💡 Enfoque técnico: Programación Defensiva (Máquina de Estados)
Los métodos del dron actúan como una máquina de estados finitos. En el método `acelerar` o `girar`, el primer paso algorítmico es verificar el atributo `_en_vuelo`. Si el dron está aterrizado, la capa de dominio rechaza la operación levantando un `ValueError` descriptivo. El cliente/interfaz (`Main.py`) captura este error y lo informa al usuario, impidiendo que los datos internos del objeto se corrompan por acciones ilógicas.

---

## 💻 Simulación de Ejecución en Consola

```text

==============================
 SISTEMA DE CONTROL DE DRONES
==============================
1. Tricóptero
2. Cuadricóptero
3. Hexacóptero
4. Octocóptero
5. Dron Coaxial
6. Salir

Seleccione unidad a desplegar: 3

📡 Conexión establecida con la unidad.

         PANEL DE CONTROL
=================================
 Unidad Activa: Hexacoptero 🎮🚁

1. Despegar  |  2. Aterrizar
3. Acelerar  |  4. Frenar
5. Girar     |  6. Sacar Foto
7. Cambiar de Dron

[Comando]> 3
   > Incremento (km/h): 50
❌ ALERTA DE SISTEMA: Física inválida: No se puede acelerar en tierra. Despegue primero.

         PANEL DE CONTROL
=================================
 Unidad Activa: Hexacoptero 🎮🚁

1. Despegar  |  2. Aterrizar
3. Acelerar  |  4. Frenar
5. Girar     |  6. Sacar Foto
7. Cambiar de Dron

[Comando]> 1
✅ Iniciando 6 rotores. Hexacóptero despegando.

         PANEL DE CONTROL
=================================
 Unidad Activa: Hexacoptero 🎮🚁

1. Despegar  |  2. Aterrizar
3. Acelerar  |  4. Frenar
5. Girar     |  6. Sacar Foto
7. Cambiar de Dron

[Comando]> 3
   > Incremento (km/h): 50
✅ Hexacóptero acelerando. Velocidad actual: 50 km/h.

         PANEL DE CONTROL
=================================
 Unidad Activa: Hexacoptero 🎮🚁

1. Despegar  |  2. Aterrizar
3. Acelerar  |  4. Frenar
5. Girar     |  6. Sacar Foto
7. Cambiar de Dron

[Comando]> 5
   > Dirección (derecha/izquierda): derecha
✅ Hexacóptero rotando sobre su eje hacia la derecha.

         PANEL DE CONTROL
=================================
 Unidad Activa: Hexacoptero 🎮🚁

1. Despegar  |  2. Aterrizar
3. Acelerar  |  4. Frenar
5. Girar     |  6. Sacar Foto
7. Cambiar de Dron

[Comando]> 6
✅ 📸 Clic! Captura aérea realizada desde el Hexacóptero.

         PANEL DE CONTROL
=================================
 Unidad Activa: Hexacoptero 🎮🚁

1. Despegar  |  2. Aterrizar
3. Acelerar  |  4. Frenar
5. Girar     |  6. Sacar Foto
7. Cambiar de Dron

[Comando]> 2
✅ Hexacóptero aterrizado con éxito. Rotores apagados.

         PANEL DE CONTROL
=================================
 Unidad Activa: Hexacoptero 🎮🚁

1. Despegar  |  2. Aterrizar
3. Acelerar  |  4. Frenar
5. Girar     |  6. Sacar Foto
7. Cambiar de Dron

[Comando]> 7

==============================
 SISTEMA DE CONTROL DE DRONES
==============================
1. Tricóptero
2. Cuadricóptero
3. Hexacóptero
4. Octocóptero
5. Dron Coaxial
6. Salir

Seleccione unidad a desplegar: 6

Apagando sistema de control de drones. ¡Hasta la próxima! 👋