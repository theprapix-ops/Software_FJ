
from modelos.reserva import Reserva

from utilidades.excepciones import (
    ClienteNoEncontradoError,
    ServicioNoEncontradoError,
    ReservaNoEncontradaError,
    OperacionInvalidaError
)

from utilidades.registro import (
    registrar_operacion,
    registrar_error
)


class GestorSistema:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    # -------------------------------
    # GESTIÓN DE CLIENTES
    # -------------------------------

    def registrar_cliente(self, cliente):
        try:
            if cliente is None:
                raise ValueError("El cliente no puede estar vacío.")

            if any(
                c.identificacion == cliente.identificacion
                for c in self.clientes
            ):
                raise OperacionInvalidaError(
                    "El cliente ya está registrado."
                )

            self.clientes.append(cliente)

        except Exception as error:
            registrar_error("Error al registrar un cliente.")

            raise OperacionInvalidaError(
                "No fue posible registrar el cliente."
            ) from error

        else:
            registrar_operacion(
                f"Cliente registrado: {cliente.identificacion}"
            )

            return "Cliente registrado correctamente."

    def buscar_cliente(self, identificacion):
        if (
            not isinstance(identificacion, str)
            or not identificacion.strip()
        ):
            raise ValueError(
                "La identificación debe ser un texto válido."
            )

        for cliente in self.clientes:
            if cliente.identificacion == identificacion.strip():
                return cliente

        error = ClienteNoEncontradoError(
            f"No existe el cliente con identificación {identificacion}."
        )

        registrar_error("Búsqueda de cliente fallida.")
        raise error

    def listar_clientes(self):
        return self.clientes

    # -------------------------------
    # GESTIÓN DE SERVICIOS
    # -------------------------------

    def registrar_servicio(self, servicio):
        try:
            if servicio is None:
                raise ValueError("El servicio no puede estar vacío.")

            if any(
                s.nombre.lower() == servicio.nombre.lower()
                for s in self.servicios
            ):
                raise OperacionInvalidaError(
                    "El servicio ya está registrado."
                )

            self.servicios.append(servicio)

        except Exception as error:
            registrar_error("Error al registrar un servicio.")

            raise OperacionInvalidaError(
                "No fue posible registrar el servicio."
            ) from error

        else:
            registrar_operacion(
                f"Servicio registrado: {servicio.nombre}"
            )

            return "Servicio registrado correctamente."

    def buscar_servicio(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError(
                "El nombre del servicio no es válido."
            )

        for servicio in self.servicios:
            if servicio.nombre.lower() == nombre.strip().lower():
                return servicio

        error = ServicioNoEncontradoError(
            f"No existe el servicio {nombre}."
        )

        registrar_error("Búsqueda de servicio fallida.")
        raise error

    def listar_servicios(self):
        return self.servicios

    # -------------------------------
    # GESTIÓN DE RESERVAS
    # -------------------------------

    def crear_reserva(
        self,
        identificacion,
        nombre_servicio,
        duracion
    ):
        try:
            cliente = self.buscar_cliente(identificacion)
            servicio = self.buscar_servicio(nombre_servicio)

            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            self.reservas.append(reserva)

        except Exception as error:
            registrar_error("Error al crear una reserva.")

            raise OperacionInvalidaError(
                "No fue posible crear la reserva."
            ) from error

        else:
            registrar_operacion(
                f"Reserva creada para el cliente {identificacion}"
            )

            return reserva

    def buscar_reserva(self, posicion):
        if (
            not isinstance(posicion, int)
            or isinstance(posicion, bool)
            or posicion < 1
        ):
            error = ReservaNoEncontradaError(
                "Número de reserva inválido."
            )

            registrar_error(
                "Búsqueda de reserva con número inválido."
            )

            raise error

        if posicion > len(self.reservas):
            error = ReservaNoEncontradaError(
                "La reserva no existe."
            )

            registrar_error(
                "Búsqueda de reserva inexistente."
            )

            raise error

        return self.reservas[posicion - 1]

    def confirmar_reserva(self, posicion):
        reserva = self.buscar_reserva(posicion)

        try:
            resultado = reserva.confirmar()

        except ValueError as error:
            registrar_error("Error al confirmar una reserva.")

            raise OperacionInvalidaError(
                str(error)
            ) from error

        else:
            registrar_operacion(
                f"Reserva {posicion} confirmada."
            )

            return resultado

        finally:
            print(
                "Verificación de confirmación finalizada."
            )

    def cancelar_reserva(self, posicion):
        reserva = self.buscar_reserva(posicion)

        try:
            resultado = reserva.cancelar()

        except ValueError as error:
            registrar_error("Error al cancelar una reserva.")

            raise OperacionInvalidaError(
                str(error)
            ) from error

        else:
            registrar_operacion(
                f"Reserva {posicion} cancelada."
            )

            return resultado

        finally:
            print(
                "Verificación de cancelación finalizada."
            )

    def procesar_reserva(self, posicion):
        reserva = self.buscar_reserva(posicion)

        try:
            costo = reserva.procesar()

        except ValueError as error:
            registrar_error("Error al procesar una reserva.")

            raise OperacionInvalidaError(
                str(error)
            ) from error

        else:
            registrar_operacion(
                f"Reserva {posicion} procesada."
            )

            return costo

        finally:
            print(
                "Verificación del procesamiento finalizada."
            )

    def listar_reservas(self):
        return self.reservas

