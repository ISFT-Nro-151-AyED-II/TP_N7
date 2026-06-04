class Animal:
    """
    Contrato base (Interface). 
    En sistemas de producción, no confiamos ciegamente en el Duck Typing de Python.
    Exigimos una estructura base para asegurar que el polimorfismo no falle en runtime.
    """
    def hablar(self) -> str:
        raise NotImplementedError("Las subclases deben implementar la lógica de hablar()")

class Perro(Animal):
    def hablar(self) -> str:
        return "Guau!"

class Gato(Animal):
    def hablar(self) -> str:
        return "Miau!"

class Dron:
    """
    Entidad intrusa y ajena a la jerarquía 'Animal'. 
    Se crea a propósito para probar la robustez del ciclo for polimórfico en el main.
    """
    def volar(self) -> str:
        return "Zumbido de hélices..."