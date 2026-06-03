import sys
from Calculadora import Calculadora

def solicitar_input_numerico(prompt: str) -> float:
    """
    Aísla el ciclo de solicitud de datos para no repetir bloques try-except 
    cada vez que pedimos un operando.
    """
    while True:
        valor = input(prompt)
        try:
            # Consumimos el método estático para la validación.
            return Calculadora.validar_numero(valor)
        except ValueError as e:
            print(f"\n⚠️ Error de validación: {e}. Reintentá.")

def ejecutar_cli():
    print("\nIniciando Sistema de Cálculo...")
    calc = Calculadora("Sesion_CLI_Principal")
    
    while True:
        print("\n================")
        print(" MENÚ PRINCIPAL ")
        print("================\n")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver estadísticas e historial")
        print("6. Salir")
        
        opcion = input("\nSeleccioná una operación (1-6): ").strip() 
        # .strip() para eliminar espacios en blanco por si el usuario los ingresa accidentalmente.
        
        if opcion == '6':
            print("\nCerrando sesión. Fin de la ejecución.")
            sys.exit(0)
            
        if opcion == '5':
            print(f"\nHISTORIAL LOCAL (Sesión: {calc.identificador_sesion}) ")
            print("===============================================\n")

            for item in calc.historial_local:
                print(f" - {item}")
            # Consumimos el método de clase.
            print(f"> Total operaciones globales procesadas por la Clase: {Calculadora.obtener_estadisticas_globales()}")
            continue

        if opcion not in ['1', '2', '3', '4']:
            print("\n⚠️ Opción inválida. Seleccioná un número del 1 al 6.")
            continue

        # Ingreso de datos.
        op1 = solicitar_input_numerico("\nIngresá el primer valor: ")
        op2 = solicitar_input_numerico("\nIngresá el segundo valor: ")

        # Procesamiento y manejo de errores de lógica
        try:
            if opcion == '1':
                res = calc.sumar(op1, op2)
            elif opcion == '2':
                res = calc.restar(op1, op2)
            elif opcion == '3':
                res = calc.multiplicar(op1, op2)
            elif opcion == '4':
                res = calc.dividir(op1, op2)
            
            print(f"\n✅ Resultado exitoso: {res}")
            
        except ZeroDivisionError as e:
            print(f"\n❌ Error de ejecución: {e}")
        except Exception as e:
            # Captura de contingencia por si se escapa alguna excepción no controlada
            print(f"\n❌ Error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_cli()