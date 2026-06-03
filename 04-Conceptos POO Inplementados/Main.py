import sys
from JerarquiaAnimal import Animal, Perro, Vaca, Abeja

# [COHESIÓN DÉBIL (EVITADA)]: 
# Si metiéramos los prints, los inputs de consola y la lógica de validación de negocio 
# todo mezclado dentro de las clases de 'JerarquiaAnimal.py', tendríamos Cohesión Débil. 
# Separar la I/O (Main) del modelo de dominio (JerarquiaAnimal) garantiza Cohesión Fuerte en ambos módulos.

def mostrar_menu():
    print("\n" + "="*36)
    print(" SISTEMA DE GESTIÓN (CONCEPTOS POO) ")
    print("="*36 + "\n")
    print("1. Instanciar e interactuar (Prueba de Fatiga)")
    print("2. Inspeccionar metadatos de herencia")
    print("3. Salir")

def interactuar_animales():
    # [ACOPLAMIENTO BAJO]: Usamos un diccionario como Factory. 
    # El menú no depende de bloques 'if/elif' rígidos atados a clases específicas.
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
            raise ValueError("Opción fuera de rango. No corresponde a un animal válido.")
            
        nombre_animal = input("\nIngresá un nombre para el animal: ").strip()
        if not nombre_animal:
            raise ValueError("El nombre es obligatorio para la instanciación.")

        _, clase_elegida = registro_clases[opcion]
        instancia = clase_elegida(nombre_animal)
        
        print("\n✅ Objeto instanciado correctamente")
        print("=" * 36 + "\n")
        print(instancia.describirme())
        
        # Simulamos interacción continua para probar el encapsulamiento y el desgaste de energía.
        for i in range(3):
            print(f"\n[Acción {i+1}]")
            print(f"Hablar: {instancia.accionar_hablar()}")
            print(f"Moverse: {instancia.accionar_moverse()}")
            print(f"> Energía restante: {instancia.energia}%")
            
    except Exception as e:
        print(f"\n❌ Error de ejecución: {e}")

def inspeccionar_metadatos():
    print("\n METADATOS E INTROSPECCIÓN ")
    print("="*30)
    try:
        print(f"> Tupla __bases__ de Perro: {Perro.__bases__}")
        print(f"> Subclases de Animal: {[sub.__name__ for sub in Animal.__subclasses__()]}")
        print(f"> Atributo __base__ de Vaca: {Vaca.__base__}")
    except AttributeError as e:
        print(f"\n❌ Error de introspección: {e}")

def ejecutar_cli():
    while True:
        mostrar_menu()
        seleccion = input("\nElegí una opción: ").strip()
        
        if seleccion == '1':
            interactuar_animales()
        elif seleccion == '2':
            inspeccionar_metadatos()
        elif seleccion == '3':
            print("\nCerrando sistema.")
            sys.exit(0)
        else:
            print("\n⚠️ Opción inválida. Reintentá.")

if __name__ == "__main__":
    ejecutar_cli()