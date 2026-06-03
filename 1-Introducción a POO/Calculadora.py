class Calculadora:
    """
    Gestiona operaciones aritméticas básicas.
    Se aísla la lógica matemática y de validación del manejo de la interfaz (I/O).
    """
    # Atributo de clase: Compartido por todas las instancias. 
    # Útil para auditoría o métricas de uso global en un sistema más grande.
    total_operaciones_globales = 0 

    def __init__(self, identificador_sesion: str):
        # Atributos de instancia: Estado propio de cada objeto creado.
        self.identificador_sesion = identificador_sesion
        self.historial_local = [] # Se guarda en una lista.

    @staticmethod
    def validar_numero(valor) -> float:
        """
        Método estático: No necesita acceder ni modificar el estado de la instancia (self) 
        ni de la clase (cls). Es una función utilitaria encapsulada lógicamente acá.
        """
        try:
            # Reemplazamos comas por puntos previendo el input clásico del usuario local.
            valor_formateado = str(valor).replace(',', '.')
            return float(valor_formateado)
        except ValueError:
            # Lanzamos la excepción hacia arriba para que la capa de interfaz decida cómo manejarla.
            raise ValueError(f"El valor ingresado ('{valor}') no es numérico.")

    @classmethod
    def obtener_estadisticas_globales(cls) -> int:
        """
        Método de clase: Accede al estado global de la clase (cls). 
        Permite consultar métricas sin instanciar la calculadora o desde cualquier instancia.
        """
        return cls.total_operaciones_globales

    def _registrar_operacion(self, detalle: str):
        """
        Método de instancia privado (convención _).
        Mantiene la cohesión actualizando tanto el estado local como el global en un solo lugar.
        """
        self.historial_local.append(detalle)
        Calculadora.total_operaciones_globales += 1

    # Métodos de instancia: Operan con el estado del objeto.
    def sumar(self, a, b) -> float:
        num_a = self.validar_numero(a)
        num_b = self.validar_numero(b)
        resultado = num_a + num_b
        self._registrar_operacion(f"Suma: {num_a} + {num_b} = {resultado}")
        return resultado

    def restar(self, a, b) -> float:
        num_a = self.validar_numero(a)
        num_b = self.validar_numero(b)
        resultado = num_a - num_b
        self._registrar_operacion(f"Resta: {num_a} - {num_b} = {resultado}")
        return resultado

    def multiplicar(self, a, b) -> float:
        num_a = self.validar_numero(a)
        num_b = self.validar_numero(b)
        resultado = num_a * num_b
        self._registrar_operacion(f"Multiplicación: {num_a} * {num_b} = {resultado}")
        return resultado

    def dividir(self, a, b) -> float:
        num_a = self.validar_numero(a)
        num_b = self.validar_numero(b)
        
        # Programación defensiva de negocio: atajamos el error matemático antes de que el motor lo haga.
        if num_b == 0:
            raise ZeroDivisionError("Error algorítmico: Intento de división por cero.")
            
        resultado = num_a / num_b
        self._registrar_operacion(f"División: {num_a} / {num_b} = {resultado}")
        return resultado