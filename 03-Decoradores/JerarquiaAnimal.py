class Animal:
    """
    Clase base. Define el contrato y ahora encapsula el estado interno
    para garantizar la integridad de los datos.
    """
    def __init__(self, nombre: str):
        # 3.2. Implementar encapsulamiento vía "__" (Name Mangling).
        # Ocultamos el estado para evitar modificaciones no controladas desde el exterior.
        self.__nombre = nombre
        self.__energia = 100  # Valor por defecto inicial.

    # 3.1. Implementar @property (Getters).
    # Exponemos el estado a través de una interfaz de lectura controlada.
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def energia(self) -> int:
        return self.__energia

    # 3.3. Implementar setter().
    # Centralizamos las reglas de negocio en la asignación de variables.
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("Inconsistencia: El nombre no puede estar vacío ni contener solo espacios.")
        self.__nombre = nuevo_nombre

    @energia.setter
    def energia(self, nivel: int):
        if not (0 <= nivel <= 100):
            # Programación defensiva a nivel de modelo de dominio.
            raise ValueError("Regla de negocio vulnerada: La energía debe estar entre 0 y 100.")
        self.__energia = nivel

    def hablar(self) -> str:
        raise NotImplementedError("La subclase debe implementar el método hablar()")

    def moverse(self) -> str:
        raise NotImplementedError("La subclase debe implementar el método moverse()")

    def describirme(self) -> str:
        return f"Soy {self.__nombre}, un objeto de la clase {type(self).__name__}."


class Perro(Animal):
    def hablar(self) -> str:
        return "Guau!"

    def moverse(self) -> str:
        return "Caminando con 4 patas"


class Vaca(Animal):
    def hablar(self) -> str:
        return "Muuu!"

    def moverse(self) -> str:
        return "Caminando con 4 patas"


class Abeja(Animal):
    def hablar(self) -> str:
        return "Bzzzz!"

    def moverse(self) -> str:
        return "Volando"