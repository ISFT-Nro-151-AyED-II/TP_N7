import sys
from Entidades import Pato, Leon, Grillo, Pez

def mostrar_menu():
    print("\n" + "="*33)
    print(" MOTOR DE EJECUCIÓN: DUCK TYPING ")
    print("="*33)
    print("1. Agregar Pato a la cola")
    print("2. Agregar León a la cola")
    print("3. Agregar Grillo a la cola")
    print("4. Agregar Pez (Entidad sin sonido) a la cola")
    print("5. Ejecutar acciones en lote (Duck Typing)")
    print("6. Salir")

def procesar_lote(lista_animales: list):
    """
    Recibe una lista heterogénea y ejecuta el comportamiento deseado.
    El algoritmo no pregunta "Qué sos", sino "Qué sabés hacer".
    """
    if not lista_animales:
        print("\n⚠️ Operación abortada: La lista está vacía. Cargá entidades primero.")
        return

    print("\nINICIANDO PROCESAMIENTO POR DUCK TYPING")
    print("="*40 + "\n")
    for indice, entidad in enumerate(lista_animales):
        try:
            # PROGRAMACIÓN DEFENSIVA (Look Before You Leap):
            # En lugar de usar un bloque try...except a ciegas para cazar el AttributeError,
            # consultamos dinámicamente si el objeto posee la capacidad requerida.
            # Esto evita saturar el stack de excepciones del motor de Python.
            if not hasattr(entidad, 'emitir_sonido') or not callable(getattr(entidad, 'emitir_sonido')):
                raise AttributeError(f"Incompatibilidad detectada: {type(entidad).__name__} no posee la capacidad 'emitir_sonido()'.")
            
            # Ejecución dinámica. El intérprete resuelve en tiempo real a qué clase pertenece.
            resultado = entidad.emitir_sonido()
            print(f"[{type(entidad).__name__}] -> {resultado}")

        except AttributeError as e:
            # Capturamos el error estructural para aislar la entidad y continuar con el lote.
            print(f"❌ [Error de Comportamiento Lote #{indice}]: {e}")
        except Exception as e:
            print(f"❌ [Falla Crítica del Sistema]: {e}")
            
    print("\n--- FIN DEL PROCESAMIENTO ---")

def ejecutar_cli():
    # Inicialización de la estructura de datos que almacenará las entidades en memoria.
    cola_procesamiento = []
    
    # Factory simplificado para evitar un bloque gigante de condicionales en la carga.
    catalogo = {
        '1': Pato,
        '2': Leon,
        '3': Grillo,
        '4': Pez
    }
    
    while True:
        mostrar_menu()
        seleccion = input("\n[Sistema]> Elegí una opción: ").strip()
        
        if seleccion == '6':
            print("\nVaciando memoria y cerrando sistema.")
            sys.exit(0)
            
        if seleccion == '5':
            procesar_lote(cola_procesamiento)
            # Limpiamos la cola post-procesamiento para el siguiente lote.
            cola_procesamiento.clear() 
            continue
            
        try:
            if seleccion not in catalogo:
                raise ValueError("La opción ingresada no es válida en el catálogo actual.")
            
            # Instanciación dinámica y anexado a la lista.
            nueva_entidad = catalogo[seleccion]()
            cola_procesamiento.append(nueva_entidad)
            print(f"✅ {type(nueva_entidad).__name__} agregado a la cola de procesamiento. (Total en cola: {len(cola_procesamiento)})")
            
        except ValueError as e:
            print(f"\n⚠️ Error de carga: {e}")

if __name__ == "__main__":
    ejecutar_cli()