import sys
from Modelos import Animal, Perro, Gato, Dron

def procesar_sonidos():
    # El iterador de la consigna evalúa una colección.
    # Inyectamos objetos válidos y un intruso (Dron) para someter el algoritmo a estrés.
    entidades = [Perro(), Gato(), Dron()]
    
    print("\n"+"="*23)
    print(" EJECUCIÓN POLIMÓRFICA ")
    print("="*23+"\n")
    
    # Análisis y ejecución del "for" solicitado en la consigna.
    for entidad in entidades:
        try:
            # PROGRAMACIÓN DEFENSIVA:
            # Validamos pertenencia al contrato antes de invocar el método.
            # Esto previene que un objeto sin el método 'hablar()' genere un volcado de memoria (crash).
            if not isinstance(entidad, Animal):
                raise TypeError(f"Inconsistencia: El objeto de clase '{type(entidad).__name__}' no respeta el contrato 'Animal'.")
                
            # Llamado Polimórfico: Un mismo mensaje ('hablar()') genera comportamientos 
            # dinámicos según el tipo de dato subyacente alojado en la variable 'entidad'.
            sonido = entidad.hablar()
            print(f"> [{type(entidad).__name__}] emitió el sonido: {sonido}")
            
        except TypeError as e:
            # Capturamos el error de diseño para que el ciclo siga procesando los demás objetos.
            print(f"❌ Error de Integridad: {e}")
        except Exception as e:
            print(f"❌ Falla de sistema inesperada: {e}")

if __name__ == "__main__":
    procesar_sonidos()
    sys.exit(0)