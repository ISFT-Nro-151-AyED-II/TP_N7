class Pato:
    """Entidad estándar. Cumple con el comportamiento esperado."""
    def emitir_sonido(self) -> str:
        return "Cuac cuac!"

class Leon:
    """Entidad independiente. Sin relación estructural con Pato."""
    def emitir_sonido(self) -> str:
        return "Roaar!"

class Grillo:
    """Entidad independiente. Su implementación de sonido es diferente."""
    def emitir_sonido(self) -> str:
        return "Cri cri cri..."

class Pez:
    """
    Entidad anómala (intruso). 
    Se introduce intencionalmente sin el método 'emitir_sonido' para probar 
    la resiliencia de la iteración por Duck Typing en la capa superior.
    """
    def nadar(self) -> str:
        return "Glu glu..."