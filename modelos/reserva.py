
class Reserva:

    ESTADOS_VALIDOS = ("Pendiente", "Confirmada", "Cancelada", "Procesada")

    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ValueError("La reserva necesita un cliente.")

        if servicio is None:
            raise ValueError("La reserva necesita un servicio.")

        if (not isinstance(duracion, (int, float))
                or isinstance(duracion, bool)
                or duracion <= 0):
            raise ValueError("La duración debe ser un número mayor que cero.")

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ValueError("Solo se pueden confirmar reservas pendientes.")

        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        if self.__estado != "Pendiente":
            raise ValueError("Solo se pueden cancelar reservas pendientes.")

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        if self.__estado != "Confirmada":
            raise ValueError("La reserva debe estar confirmada para procesarse.")

        costo = self.__servicio.calcular_costo(self.__duracion)
        self.__estado = "Procesada"
        return costo

    def mostrar_reserva(self):
        return (
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion}\n"
            f"Estado: {self.__estado}"
        )
