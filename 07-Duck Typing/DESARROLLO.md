# Resolución TP N°7 - Implementación de Duck Typing

## 💡 Enfoque técnico: Ausencia de Contratos (Tipado Dinámico Puro)
En este ejercicio se descartó deliberadamente el uso de superclases abstractas (`abc.ABC`) o interfaces jerárquicas. Las entidades (`Pato`, `Leon`, `Grillo`, `Pez`) existen en paralelo sin un ancestro común (más allá del `object` nativo de Python). La decisión arquitectónica central radica en que la función `procesar_lote` itera sobre la lista y ejecuta el método `emitir_sonido()` guiándose exclusivamente por la filosofía de **Duck Typing**: el programa evalúa qué es capaz de hacer el objeto en tiempo de ejecución, ignorando por completo qué tipo de clase es. Esto reduce drásticamente el acoplamiento y fomenta una extrema flexibilidad en el paso de mensajes.

## 💡 Enfoque técnico: Resiliencia vía Introspección (`hasattr`)
El mayor riesgo del Duck Typing en entornos de producción es inyectar un objeto en el flujo de ejecución que carezca del comportamiento esperado, lo que detiene el motor del lenguaje al arrojar un `AttributeError`. Para construir un código robusto, se implementó el paradigma **LBYL** (*Look Before You Leap* - Mirar antes de saltar) en lugar de **EAFP** (*Easier to Ask for Forgiveness than Permission*). 
Al usar la función nativa `hasattr(entidad, 'emitir_sonido')`, validamos introspectivamente si el objeto en memoria cumple con el requerimiento de comportamiento *antes* de enviarle el mensaje. Si falla, se arroja una excepción controlada que permite descartar al objeto incompatible (como la instancia de `Pez`) sin abortar el procesamiento del resto del lote.

---

## 💻 Simulación de Ejecución en Consola

```text

=================================
 MOTOR DE EJECUCIÓN: DUCK TYPING
=================================
1. Agregar Pato a la cola
2. Agregar León a la cola
3. Agregar Grillo a la cola
4. Agregar Pez (Entidad sin sonido) a la cola
5. Ejecutar acciones en lote (Duck Typing)
6. Salir

[Sistema]> Elegí una opción: 5

⚠️ Operación abortada: La lista está vacía. Cargá entidades primero.

=================================
 MOTOR DE EJECUCIÓN: DUCK TYPING
=================================
1. Agregar Pato a la cola
2. Agregar León a la cola
3. Agregar Grillo a la cola
4. Agregar Pez (Entidad sin sonido) a la cola
5. Ejecutar acciones en lote (Duck Typing)
6. Salir

[Sistema]> Elegí una opción: 1
✅ Pato agregado a la cola de procesamiento. (Total en cola: 1)

=================================
 MOTOR DE EJECUCIÓN: DUCK TYPING
=================================
1. Agregar Pato a la cola
2. Agregar León a la cola
3. Agregar Grillo a la cola
4. Agregar Pez (Entidad sin sonido) a la cola
5. Ejecutar acciones en lote (Duck Typing)
6. Salir

[Sistema]> Elegí una opción: 2
✅ Leon agregado a la cola de procesamiento. (Total en cola: 2)

=================================
 MOTOR DE EJECUCIÓN: DUCK TYPING
=================================
1. Agregar Pato a la cola
2. Agregar León a la cola
3. Agregar Grillo a la cola
4. Agregar Pez (Entidad sin sonido) a la cola
5. Ejecutar acciones en lote (Duck Typing)
6. Salir

[Sistema]> Elegí una opción: 4
✅ Pez agregado a la cola de procesamiento. (Total en cola: 3)

=================================
 MOTOR DE EJECUCIÓN: DUCK TYPING
=================================
1. Agregar Pato a la cola
2. Agregar León a la cola
3. Agregar Grillo a la cola
4. Agregar Pez (Entidad sin sonido) a la cola
5. Ejecutar acciones en lote (Duck Typing)
6. Salir

[Sistema]> Elegí una opción: 3
✅ Grillo agregado a la cola de procesamiento. (Total en cola: 4)

=================================
 MOTOR DE EJECUCIÓN: DUCK TYPING
=================================
1. Agregar Pato a la cola
2. Agregar León a la cola
3. Agregar Grillo a la cola
4. Agregar Pez (Entidad sin sonido) a la cola
5. Ejecutar acciones en lote (Duck Typing)
6. Salir

[Sistema]> Elegí una opción: 5

INICIANDO PROCESAMIENTO POR DUCK TYPING
========================================

[Pato] -> Cuac cuac!
[Leon] -> Roaar!
❌ [Error de Comportamiento Lote #2]: Incompatibilidad detectada: Pez no posee la capacidad 'emitir_sonido()'.
[Grillo] -> Cri cri cri...

--- FIN DEL PROCESAMIENTO ---

=================================
 MOTOR DE EJECUCIÓN: DUCK TYPING
=================================
1. Agregar Pato a la cola
2. Agregar León a la cola
3. Agregar Grillo a la cola
4. Agregar Pez (Entidad sin sonido) a la cola
5. Ejecutar acciones en lote (Duck Typing)
6. Salir

[Sistema]> Elegí una opción: 6

Vaciando memoria y cerrando sistema.