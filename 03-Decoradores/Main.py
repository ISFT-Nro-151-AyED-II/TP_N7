import sys
from JerarquiaAnimal import Animal, Perro, Vaca, Abeja

def mostrar_menu():
    print("\n" + "="*32)
    print(" SISTEMA DE GESTIÓN DE HERENCIA ")
    print("="*32 + "\n")
    print("1. Instanciar e interactuar con animales.")
    print("2. Inspeccionar metadatos de herencia.")
    print("3. Salir")

def interactuar_animales():
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
            raise ValueError("La opción seleccionada no corresponde a un animal válido.")
            
        nombre_animal = input("\nIngresá un nombre para el animal: ").strip()
        if not nombre_animal:
            # Validación rápida en la capa de interfaz.
            raise ValueError("El nombre es obligatorio para la instanciación.")

        # Instanciación dinámica pasando el parámetro requerido por el nuevo constructor.
        _, clase_elegida = registro_clases[opcion]
        instancia = clase_elegida(nombre_animal)
        
        print("\n✅ Objeto instanciado correctamente.")
        print(f"\nDescribirme: {instancia.describirme()}")
        print(f"Hablar: {instancia.hablar()}")
        print(f"Moverse: {instancia.moverse()}")
        
        # Prueba de métodos decorados
        print(f"\n[Prueba de Property] Energía actual de {instancia.nombre}: {instancia.energia}%")
        nueva_energia = input(f"\nIngresá nueva energía para {instancia.nombre} (0-100) para probar el Setter: ").strip()
        
        if not nueva_energia.isdigit() and not (nueva_energia.startswith('-') and nueva_energia[1:].isdigit()):
            raise ValueError("El valor de energía debe ser numérico.")
            
        # Ejecución del setter (la validación de negocio 0-100 la hace la clase, no el main).
        instancia.energia = int(nueva_energia)
        print(f"\n✅ [Prueba de Setter exitosa] Nueva energía registrada: {instancia.energia}%")
        
    except Exception as e:
        # Programación defensiva centralizada para esta operación.
        print(f"\n❌ Error durante la interacción: {e}")

def inspeccionar_metadatos():
    print("\n METADATOS E INTROSPECCIÓN DE CLASES ")
    print("="*37 + "\n")
    try:
        print(f"> Tupla __bases__ de Perro: {Perro.__bases__}")
        print(f"> Subclases de Animal: {[sub.__name__ for sub in Animal.__subclasses__()]}")
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