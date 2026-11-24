
from modelos.servicio import Servicio


class ServicioSala(Servicio):

    def __init__(self, tarifa_base, capacidad):
        super().__init__("Reserva de sala", tarifa_base)

        if (not isinstance(capacidad, int)
                or isinstance(capacidad, bool)
                or capacidad <= 0):
            raise ValueError("La capacidad debe ser un entero positivo.")

        self.__capacidad = capacidad

    def validar_parametros(self, duracion):
        if (not isinstance(duracion, (int, float))
                or isinstance(duracion, bool)
                or duracion <= 0):
            raise ValueError("La duración debe ser un número positivo.")

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        return self.calcular_total(duracion, impuesto, descuento)

    def describir_servicio(self):
        return (
            f"{self.nombre}. Capacidad máxima: "
            f"{self.__capacidad} personas."
        )
