import sys
from Modelos import Tricoptero, Cuadricoptero, Hexacoptero, Octocoptero, Coaxial
from Contratos import IPilotable

def menu_principal():
    print("\n" + "="*30)
    print(" SISTEMA DE CONTROL DE DRONES ")
    print("="*30)
    print("1. Tricóptero")
    print("2. Cuadricóptero")
    print("3. Hexacóptero")
    print("4. Octocóptero")
    print("5. Dron Coaxial")
    print("6. Salir")

def menu_vuelo(dron: IPilotable):
    """
    Este controlador depende únicamente de la abstracción (IPilotable).
    Ignora completamente qué modelo de dron físico está operando (Polimorfismo).
    """
    while True:
        
        print(f"\n         PANEL DE CONTROL")
        print("="*33)
        print(f" Unidad Activa: {dron.__class__.__name__} 🎮🚁\n")
        print("1. Despegar  |  2. Aterrizar")
        print("3. Acelerar  |  4. Frenar")
        print("5. Girar     |  6. Sacar Foto")
        print("7. Cambiar de Dron")
        
        comando = input("\n[Comando]> ").strip()
        
        try:
            if comando == '1':
                print(f"✅ {dron.despegar()}")
            elif comando == '2':
                print(f"✅ {dron.aterrizar()}")
            elif comando == '3':
                val = input("   > Incremento (km/h): ")
                # Validación de casteo.
                if not val.isdigit(): raise ValueError("El valor debe ser entero.")
                print(f"✅ {dron.acelerar(int(val))}")
            elif comando == '4':
                print(f"✅ {dron.frenar()}")
            elif comando == '5':
                dir = input("   > Dirección (derecha/izquierda): ")
                print(f"✅ {dron.girar(dir)}")
            elif comando == '6':
                print(f"✅ {dron.sacar_foto()}")
            elif comando == '7':
                # Salimos del sub-menú para volver al hangar.
                break
            else:
                print("⚠️ Comando no reconocido.")
                
        except ValueError as e:
            # Capturamos las excepciones de regla de negocio lanzadas por el modelo.
            print(f"❌ ALERTA DE SISTEMA: {e}")
        except Exception as e:
            print(f"❌ FALLA CRÍTICA: {e}")

def ejecutar_cli():
    hangar = {
        '1': Tricoptero,
        '2': Cuadricoptero,
        '3': Hexacoptero,
        '4': Octocoptero,
        '5': Coaxial
    }
    
    while True:
        menu_principal()
        seleccion = input("\nSeleccione unidad a desplegar: ").strip()
        
        if seleccion == '6':
            print("\nApagando sistema de control de drones. ¡Hasta la próxima! 👋\n")
            sys.exit(0)
            
        try:
            if seleccion not in hangar:
                raise ValueError("Unidad no disponible en hangar.")
                
            # Instanciamos el dron seleccionado dinámicamente.
            dron_activo = hangar[seleccion]()
            print(f"\n📡 Conexión establecida con la unidad.")
            
            # Pasamos la instancia al controlador de vuelo.
            menu_vuelo(dron_activo)
            
        except ValueError as e:
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    ejecutar_cli()