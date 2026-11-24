from modelos.entidad import Entidad


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del cliente es obligatorio.")

        if not isinstance(correo, str) or "@" not in correo:
            raise ValueError("El correo electrónico no es válido.")

        if not isinstance(telefono, str) or not telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        self.__nombre = nombre.strip()
        self.__correo = correo.strip()
        self.__telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )