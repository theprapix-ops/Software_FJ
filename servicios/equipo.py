
from modelos.servicio import Servicio


class ServicioEquipo(Servicio):

    def __init__(self, tarifa_base, nombre_equipo):
        super().__init__("Alquiler de equipos", tarifa_base)

        if not isinstance(nombre_equipo, str) or not nombre_equipo.strip():
            raise ValueError("Debe indicar el nombre del equipo.")

        self.__nombre_equipo = nombre_equipo.strip()

    def validar_parametros(self, duracion):
        if (not isinstance(duracion, (int, float))
                or isinstance(duracion, bool)
                or duracion <= 0):
            raise ValueError(
                "La duración del alquiler debe ser un número positivo."
            )

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        return self.calcular_total(duracion, impuesto, descuento)

    def describir_servicio(self):
        return (
            f"{self.nombre}. Equipo disponible: "
            f"{self.__nombre_equipo}."
        )
