class Animal:
    """
    Clase base abstracta. Define el contrato, encapsula el estado y orquesta el comportamiento.
    """
    
    # [EFECTO MARIPOSA]: Esta constante es un punto único de falla o éxito. 
    # Si modificás este valor (ej: de 5 a 20), impacta automáticamente en la tasa 
    # de agotamiento de TODAS las subclases sin tener que tocar su código. 
    # Un pequeño cambio arquitectónico acá, propaga efectos en todo el sistema.
    TASA_FATIGA_BASE = 5 

    def __init__(self, nombre: str):
        # [ENCAPSULAMIENTO]: El estado interno se protege con "name mangling" (__).
        # Ningún agente externo puede corromper estas variables de forma directa.
        self.__nombre = nombre
        self.__energia = 100

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, nivel: int):
        if not (0 <= nivel <= 100):
            raise ValueError("Regla de negocio vulnerada: La energía debe estar entre 0 y 100.")
        self.__energia = nivel

    # [COHESIÓN FUERTE] + [ENCAPSULAMIENTO]: 
    # Este método hace UNA sola cosa (cohesión fuerte) y es privado (encapsulamiento).
    # Las clases externas, e incluso las hijas, no necesitan saber cómo se calcula la fatiga.
    def __consumir_energia(self, multiplicador_esfuerzo: int):
        nueva_energia = self.__energia - (multiplicador_esfuerzo * self.TASA_FATIGA_BASE)
        # Reutilizamos el setter para aprovechar su validación, aunque acá forzamos el límite inferior en 0.
        self.energia = nueva_energia if nueva_energia > 0 else 0

    # =========================================================================
    # PATRÓN TEMPLATE METHOD (Orquestación pública)
    # [ACOPLAMIENTO BAJO]: El programa principal llama a 'accionar_hablar()' 
    # sin importarle de qué clase hija es el objeto ni cómo se gasta la energía.
    # =========================================================================
    def accionar_hablar(self) -> str:
        if self.energia == 0:
            return f"{self.nombre} está demasiado exhausto para hacer ruido."
        self.__consumir_energia(1) # Hablar consume 1x de fatiga.
        return self._emitir_sonido()

    def accionar_moverse(self) -> str:
        if self.energia == 0:
            return f"{self.nombre} no tiene energía para moverse."
        self.__consumir_energia(2) # Moverse consume 2x de fatiga.
        return self._ejecutar_movimiento()

    def describirme(self) -> str:
        return f"Soy {self.nombre}, clase {type(self).__name__}. Energía vital: {self.energia}%"

    # =========================================================================
    # CONTRATOS PROTEGIDOS (Para las subclases)
    # Estos métodos usan un solo guión bajo (_) indicando que son "protected".
    # Las clases hijas DEBEN implementar la lógica específica acá.
    # =========================================================================
    def _emitir_sonido(self) -> str:
        raise NotImplementedError("Subclase debe implementar _emitir_sonido()")

    def _ejecutar_movimiento(self) -> str:
        raise NotImplementedError("Subclase debe implementar _ejecutar_movimiento()")


class Perro(Animal):
    def _emitir_sonido(self) -> str:
        return "Guau!"

    def _ejecutar_movimiento(self) -> str:
        return "Caminando con 4 patas"


class Vaca(Animal):
    def _emitir_sonido(self) -> str:
        return "Muuu!"

    def _ejecutar_movimiento(self) -> str:
        return "Caminando con 4 patas pesadamente"


class Abeja(Animal):
    def _emitir_sonido(self) -> str:
        return "Bzzzz!"

    def _ejecutar_movimiento(self) -> str:
        return "Volando"