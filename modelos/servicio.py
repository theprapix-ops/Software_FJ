
from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del servicio es obligatorio.")

        if (not isinstance(tarifa_base, (int, float))
                or isinstance(tarifa_base, bool)
                or tarifa_base <= 0):
            raise ValueError("La tarifa debe ser un número positivo.")

        self._nombre = nombre.strip()
        self._tarifa_base = tarifa_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    def calcular_total(self, duracion, impuesto=0, descuento=0):
        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        subtotal = self.tarifa_base * duracion
        total = subtotal + (subtotal * impuesto / 100)
        total -= total * descuento / 100

        return round(total, 2)

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass
