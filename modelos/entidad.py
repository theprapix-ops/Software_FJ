from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    del sistema Software FJ.
    """

    def __init__(self, identificacion):
        if not identificacion:
            raise ValueError("La identificación es obligatoria.")

        self._identificacion = identificacion

    @property
    def identificacion(self):
        return self._identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass
    