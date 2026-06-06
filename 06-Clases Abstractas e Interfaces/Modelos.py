from Contratos import IPilotable

class DronBase(IPilotable):
    """
    Clase abstracta de implementación. Resuelve la máquina de estados 
    (en vuelo / en tierra, velocidad) de forma centralizada.
    """
    def __init__(self, tipo_dron: str, rotores: int):
        self._tipo = tipo_dron
        self._rotores = rotores
        self._en_vuelo = False
        self._velocidad = 0

    # ========================================
    #  IMPLEMENTACIÓN DEL CONTRATO IPilotable
    # ========================================
    def despegar(self) -> str:
        # Lógica defensiva: Bloqueamos despegues si ya está en el aire.
        if self._en_vuelo:
            raise ValueError("Inconsistencia: El dron ya se encuentra en vuelo.")
        self._en_vuelo = True
        return f"Iniciando {self._rotores} rotores. {self._tipo} despegando."

    def aterrizar(self) -> str:
        if not self._en_vuelo:
            raise ValueError("Inconsistencia: El dron ya está en tierra.")
        self._velocidad = 0
        self._en_vuelo = False
        return f"{self._tipo} aterrizado con éxito. Rotores apagados."

    def acelerar(self, incremento: int) -> str:
        if not self._en_vuelo:
            raise ValueError("Física inválida: No se puede acelerar en tierra. Despegue primero.")
        if incremento <= 0:
            raise ValueError("El incremento de velocidad debe ser positivo.")
            
        self._velocidad += incremento
        return f"{self._tipo} acelerando. Velocidad actual: {self._velocidad} km/h."

    def frenar(self) -> str:
        if not self._en_vuelo:
            raise ValueError("Física inválida: No se puede frenar en tierra.")
        if self._velocidad == 0:
            return f"{self._tipo} ya se encuentra suspendido (Hovering)."
            
        self._velocidad = 0
        return f"{self._tipo} ha frenado. Suspendido en el aire a 0 km/h."

    def girar(self, direccion: str) -> str:
        if not self._en_vuelo:
            raise ValueError("Física inválida: No se puede girar en tierra.")
            
        dir_normalizada = direccion.strip().lower()
        if dir_normalizada not in ['derecha', 'izquierda']:
            raise ValueError("Dirección no reconocida. Use 'derecha' o 'izquierda'.")
            
        return f"{self._tipo} rotando sobre su eje hacia la {dir_normalizada}."

    def sacar_foto(self) -> str:
        # Se asume que puede sacar fotos en tierra o en vuelo, pero el mensaje cambia por contexto.
        contexto = "aérea" if self._en_vuelo else "terrestre"
        return f"📸 Clic! Captura {contexto} realizada desde el {self._tipo}."


# ==========================================
# ENTIDADES CONCRETAS
# ==========================================
class Tricoptero(DronBase):
    def __init__(self): super().__init__("Tricóptero", 3)

class Cuadricoptero(DronBase):
    def __init__(self): super().__init__("Cuadricóptero", 4)

class Hexacoptero(DronBase):
    def __init__(self): super().__init__("Hexacóptero", 6)

class Octocoptero(DronBase):
    def __init__(self): super().__init__("Octocóptero", 8)

class Coaxial(DronBase):
    def __init__(self): super().__init__("Dron Coaxial", 2)