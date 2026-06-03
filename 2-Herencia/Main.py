import sys
from JerarquiaAnimal import Animal, Perro, Vaca, Abeja

def mostrar_menu():
    print("\n" + "="*32)
    print(" SISTEMA DE GESTIÓN DE HERENCIA ")
    print("="*32 + "\n")
    print("1. Instanciar e interactuar con animales (Punto 2.5)")
    print("2. Inspeccionar metadatos de herencia (Puntos 2.3 y 2.4)")
    print("3. Salir")

def interactuar_animales():
    # Diccionario como Factory Registry para evitar múltiples if/elif y hacer el código escalable.
    registro_clases = {
        '1': ("Perro", Perro),
        '2': ("Vaca", Vaca),
        '3': ("Abeja", Abeja)
    }
    
    print("\nSeleccioná el animal a instanciar:\n")
    for clave, (nombre, _) in registro_clases.items():
        print(f"{clave}. {nombre}")
        
    opcion = input("\nOpción (1-3): ").strip()
    
    try:
        if opcion not in registro_clases:
            raise ValueError("\nLa opción seleccionada no corresponde a un animal válido.")
            
        # Instanciación dinámica.
        _, clase_elegida = registro_clases[opcion]
        instancia = clase_elegida()
        
        print("✅ Objeto instanciado correctamente.\n")
        print(f"Describirme: {instancia.describirme()}")
        print(f"Hablar: {instancia.hablar()}")
        print(f"Moverse: {instancia.moverse()}")
        
    except Exception as e:
        # Programación defensiva: capturamos cualquier fallo en la instanciación o selección.
        print(f"\n❌ Error durante la instanciación: {e}")

def inspeccionar_metadatos():
    print("\n METADATOS E INTROSPECCIÓN DE CLASES ")
    print("="*37 + "\n")
    try:
        # 2.3. Implementar __bases__ (Devuelve una tupla con las clases base directas).
        print(f"> Tupla __bases__ de Perro: {Perro.__bases__}")
        
        # 2.3. Implementar __subclasses__() (Método que lista las clases hijas activas).
        print(f"> Subclases de Animal: {[sub.__name__ for sub in Animal.__subclasses__()]}")
        
        # 2.4. Implementar base().
        # Nota técnica: Python no tiene una función nativa 'base()'. 
        # La convención para acceder a la base principal es mediante el atributo '__base__'.
        print(f"> Atributo __base__ de Vaca: {Vaca.__base__}")
        
    except AttributeError as e:
        print(f"\n❌ Error de introspección: Atributo no soportado. Detalle: {e}")

def ejecutar_cli():
    while True:
        mostrar_menu()
        seleccion = input("\nElegí una opción del menú: ").strip()
        
        if seleccion == '1':
            interactuar_animales()
        elif seleccion == '2':
            inspeccionar_metadatos()
        elif seleccion == '3':
            print("\nCerrando sistema.")
            sys.exit(0)
        else:
            print("\n⚠️ Opción inválida. Ingresá 1, 2 o 3.")

if __name__ == "__main__":
    ejecutar_cli()