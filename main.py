
from modelos.cliente import Cliente
from servicios.sala import ServicioSala
from servicios.equipo import ServicioEquipo
from servicios.asesoria import ServicioAsesoria
from servicios.gestor import GestorSistema
from utilidades.registro import configurar_registro, registrar_error


def mostrar_menu():
    print("\n========== SISTEMA SOFTWARE FJ ==========")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Registrar servicio")
    print("4. Consultar servicios")
    print("5. Crear reserva")
    print("6. Consultar reservas")
    print("7. Confirmar reserva")
    print("8. Cancelar reserva")
    print("9. Procesar reserva")
    print("10. Ejecutar demostración")
    print("0. Salir")
    print("==========================================")


def probar_calculos():
    print("\n--- PRUEBA DE CÁLCULOS DE COSTOS ---")

    sala = ServicioSala(50000, 20)

    print("Costo básico:", sala.calcular_costo(2))

    print(
        "Costo con impuesto:",
        sala.calcular_costo(2, impuesto=19)
    )

    print(
        "Costo con descuento:",
        sala.calcular_costo(2, descuento=10)
    )

    print(
        "Costo con impuesto y descuento:",
        sala.calcular_costo(
            2,
            impuesto=19,
            descuento=10
        )
    )

    print("Prueba de cálculos finalizada.")


def ejecutar_demostracion(gestor):
    print("\n--- DEMOSTRACIÓN DE OPERACIONES ---")

    try:
        # Crear un identificador único para el cliente.
        numero_cliente = 1001

        while any(
            c.identificacion == str(numero_cliente)
            for c in gestor.clientes
        ):
            numero_cliente += 1

        identificacion = str(numero_cliente)

        cliente = Cliente(
            identificacion,
            "Carlos Pérez",
            "carlos@email.com",
            "3001234567"
        )

        print(gestor.registrar_cliente(cliente))

        # Buscar servicios existentes para evitar duplicados.
        sala = next(
            (
                s for s in gestor.servicios
                if s.nombre == "Reserva de sala"
            ),
            None
        )

        equipo = next(
            (
                s for s in gestor.servicios
                if s.nombre == "Alquiler de equipos"
            ),
            None
        )

        asesoria = next(
            (
                s for s in gestor.servicios
                if s.nombre == "Servicio de asesoría"
            ),
            None
        )

        # Registrar únicamente los servicios que no existan.
        if sala is None:
            sala = ServicioSala(50000, 20)
            print(gestor.registrar_servicio(sala))

        if equipo is None:
            equipo = ServicioEquipo(25000, "Proyector")
            print(gestor.registrar_servicio(equipo))

        if asesoria is None:
            asesoria = ServicioAsesoria(
                40000,
                "Administración"
            )
            print(gestor.registrar_servicio(asesoria))

        # Crear la reserva.
        gestor.crear_reserva(
            identificacion,
            "Reserva de sala",
            2
        )

        numero_reserva = len(gestor.reservas)

        print("Reserva creada correctamente.")

        # Confirmar la reserva.
        print(gestor.confirmar_reserva(numero_reserva))

        # Procesar la reserva.
        costo = gestor.procesar_reserva(numero_reserva)

        print("Costo de la reserva:", costo)

        print("\n--- OPERACIONES CON ERRORES CONTROLADOS ---")

        # Prueba de búsqueda de cliente inexistente.
        try:
            gestor.buscar_cliente("9999")

        except Exception as error:
            registrar_error(
                f"Error de búsqueda de cliente: {error}"
            )
            print("Error de cliente controlado:", error)

        # Prueba de búsqueda de reserva inexistente.
        try:
            gestor.buscar_reserva(9999)

        except Exception as error:
            registrar_error(
                f"Error de búsqueda de reserva: {error}"
            )
            print("Error de reserva controlado:", error)

        # Prueba de registro de cliente duplicado.
        try:
            gestor.registrar_cliente(cliente)

        except Exception as error:
            registrar_error(
                f"Error de registro de cliente: {error}"
            )
            print("Error de registro controlado:", error)

        # Prueba de creación de servicio inválido.
        try:
            ServicioSala(50000, 0)

        except Exception as error:
            registrar_error(
                f"Error al crear servicio inválido: {error}"
            )
            print(
                "Error de creación de servicio controlado:",
                error
            )

        # Prueba de creación de reserva con cliente inexistente.
        try:
            gestor.crear_reserva(
                "9999",
                "Reserva de sala",
                2
            )

        except Exception as error:
            registrar_error(
                f"Error al crear reserva: {error}"
            )
            print(
                "Error de creación de reserva controlado:",
                error
            )

        # Prueba de cálculo con impuesto inválido.
        try:
            sala.calcular_costo(
                2,
                impuesto=150
            )

        except Exception as error:
            registrar_error(
                f"Error en cálculo de impuesto: {error}"
            )
            print(
                "Error de cálculo controlado:",
                error
            )

        print("\nDemostración finalizada correctamente.")

    except Exception as error:
        registrar_error(
            f"Error general en la demostración: {error}"
        )
        print(
            "No fue posible completar la demostración:",
            error
        )


def iniciar_sistema():
    configurar_registro()

    gestor = GestorSistema()

    print("======================================")
    print("       SISTEMA SOFTWARE FJ")
    print(" Gestión de Clientes, Servicios y Reservas")
    print("======================================")

    probar_calculos()

    while True:
        mostrar_menu()

        try:
            opcion = input(
                "Seleccione una opción: "
            ).strip()

            if opcion == "1":
                identificacion = input("Identificación: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                telefono = input("Teléfono: ")

                cliente = Cliente(
                    identificacion,
                    nombre,
                    correo,
                    telefono
                )

                print(
                    gestor.registrar_cliente(cliente)
                )

            elif opcion == "2":
                clientes = gestor.listar_clientes()

                if not clientes:
                    print("No hay clientes registrados.")

                for cliente in clientes:
                    print(
                        "\n",
                        cliente.mostrar_informacion()
                    )

            elif opcion == "3":
                print("\n1. Sala")
                print("2. Equipo")
                print("3. Asesoría")

                tipo = input("Tipo de servicio: ")

                tarifa = float(
                    input("Tarifa base: ")
                )

                if tipo == "1":
                    capacidad = int(
                        input("Capacidad de la sala: ")
                    )

                    servicio = ServicioSala(
                        tarifa,
                        capacidad
                    )

                elif tipo == "2":
                    nombre_equipo = input(
                        "Nombre del equipo: "
                    )

                    servicio = ServicioEquipo(
                        tarifa,
                        nombre_equipo
                    )

                elif tipo == "3":
                    especialidad = input(
                        "Especialidad: "
                    )

                    servicio = ServicioAsesoria(
                        tarifa,
                        especialidad
                    )

                else:
                    print("Tipo de servicio no válido.")
                    continue

                print(
                    gestor.registrar_servicio(servicio)
                )

            elif opcion == "4":
                servicios = gestor.listar_servicios()

                if not servicios:
                    print("No hay servicios registrados.")

                for servicio in servicios:
                    print(
                        servicio.describir_servicio()
                    )

            elif opcion == "5":
                identificacion = input(
                    "Identificación del cliente: "
                )

                nombre_servicio = input(
                    "Nombre del servicio: "
                )

                duracion = float(
                    input("Duración: ")
                )

                gestor.crear_reserva(
                    identificacion,
                    nombre_servicio,
                    duracion
                )

                print("Reserva creada correctamente.")

            elif opcion == "6":
                reservas = gestor.listar_reservas()

                if not reservas:
                    print("No hay reservas registradas.")

                for numero, reserva in enumerate(
                    reservas,
                    start=1
                ):
                    print(
                        f"\nReserva número {numero}"
                    )

                    print(
                        reserva.mostrar_reserva()
                    )

            elif opcion == "7":
                numero = int(
                    input("Número de reserva: ")
                )

                print(
                    gestor.confirmar_reserva(numero)
                )

            elif opcion == "8":
                numero = int(
                    input("Número de reserva: ")
                )

                print(
                    gestor.cancelar_reserva(numero)
                )

            elif opcion == "9":
                numero = int(
                    input("Número de reserva: ")
                )

                costo = gestor.procesar_reserva(numero)

                print(
                    f"Reserva procesada. Costo total: ${costo}"
                )

            elif opcion == "10":
                ejecutar_demostracion(gestor)

            elif opcion == "0":
                print(
                    "Gracias por utilizar Software FJ."
                )
                break

            else:
                print(
                    "Opción no válida. Intente nuevamente."
                )

        except ValueError as error:
            registrar_error(
                f"Error de dato ingresado: {error}"
            )

            print("Dato inválido:", error)

        except Exception as error:
            registrar_error(
                f"Error general del sistema: {error}"
            )

            print(
                "Se presentó un inconveniente:",
                error
            )

        finally:
            print("\nOperación finalizada.")


if __name__ == "__main__":
    iniciar_sistema()
