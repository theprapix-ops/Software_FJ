class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class ClienteNoEncontradoError(ErrorSoftwareFJ):
    """Se genera cuando no existe el cliente solicitado."""
    pass


class ServicioNoEncontradoError(ErrorSoftwareFJ):
    """Se genera cuando no existe el servicio solicitado."""
    pass


class ReservaNoEncontradaError(ErrorSoftwareFJ):
    """Se genera cuando no existe la reserva solicitada."""
    pass


class OperacionInvalidaError(ErrorSoftwareFJ):
    """Se genera cuando una operación no está permitida."""
    pass