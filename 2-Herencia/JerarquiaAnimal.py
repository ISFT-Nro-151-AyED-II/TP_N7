class Animal:
    """
    Clase base. Define el contrato que las subclases deben respetar.
    Se utiliza NotImplementedError para forzar el polimorfismo, 
    simulando el comportamiento de una clase abstracta pura sin importar el módulo abc.
    """
    def hablar(self) -> str:
        raise NotImplementedError("La subclase debe implementar el método hablar()")

    def moverse(self) -> str:
        raise NotImplementedError("La subclase debe implementar el método moverse()")

    def describirme(self) -> str:
        # Introspección dinámica: type(self).__name__ obtiene el nombre de la clase hija en tiempo de ejecución.
        return f"Soy un objeto de la clase {type(self).__name__}."


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