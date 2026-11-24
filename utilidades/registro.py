
import logging
import os


def configurar_registro():
    """Configura el archivo de registro del sistema."""

    carpeta_logs = os.path.join(
        os.path.dirname(__file__), "..", "logs"
    )
    os.makedirs(carpeta_logs, exist_ok=True)

    ruta_log = os.path.join(carpeta_logs, "software_fj.log")

    logging.basicConfig(
        filename=ruta_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        force=True
    )

    return logging.getLogger("SoftwareFJ")


def registrar_operacion(mensaje):
    """Registra operaciones exitosas del sistema."""

    logger = logging.getLogger("SoftwareFJ")
    logger.info(mensaje)


def registrar_error(mensaje):
    """Registra errores del sistema."""

    logger = logging.getLogger("SoftwareFJ")
    logger.error(mensaje)

