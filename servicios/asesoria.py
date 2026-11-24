
from modelos.servicio import Servicio


class ServicioAsesoria(Servicio):

    def __init__(self, tarifa_base, especialidad):
        super().__init__("Servicio de asesoría", tarifa_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("Debe indicar la especialidad de la asesoría.")

        self.__especialidad = especialidad.strip()

    def validar_parametros(self, duracion):
        if (not isinstance(duracion, (int, float))
                or isinstance(duracion, bool)
                or duracion <= 0):
            raise ValueError(
                "La duración de la asesoría debe ser un número positivo."
            )

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        self.validar_parametros(duracion)

        return self.calcular_total(duracion, impuesto, descuento)

    def describir_servicio(self):
        return (
            f"{self.nombre}. Especialidad: "
            f"{self.__especialidad}."
        )
