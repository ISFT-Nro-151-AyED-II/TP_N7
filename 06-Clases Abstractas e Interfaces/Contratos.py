from abc import ABC, abstractmethod

class IPilotable(ABC):
    """
    Interfaz abstracta. Define el contrato estricto de interacción.
    Cualquier clase que implemente IPilotable está obligada a desarrollar
    estos métodos, garantizando homogeneidad en el sistema.
    """
    
    @abstractmethod
    def despegar(self) -> str:
        pass
        
    @abstractmethod
    def aterrizar(self) -> str:
        pass
        
    @abstractmethod
    def acelerar(self, incremento: int) -> str:
        pass
        
    @abstractmethod
    def frenar(self) -> str:
        pass
        
    @abstractmethod
    def girar(self, direccion: str) -> str:
        pass
        
    @abstractmethod
    def sacar_foto(self) -> str:
        pass