from datetime import datetime, timedelta

from motor.compensaciones import (
    calcular_descanso_necesario,
    comprobar_duracion_compensacion,
    comprobar_compensacion,
    registrar_compensacion,
    agregar_compensacion,
    consultar_compensaciones,
    obtener_estado_compensacion,
)

def probar_calcular_descanso_necesario():

    casos = [
        timedelta(hours=14, minutes=35),
        timedelta(hours=5),
        timedelta(hours=0),
        timedelta(hours=-3)
    ]

    for horas in casos:
        try:
            resultado = calcular_descanso_necesario(horas)
            print(f"Pendiente: {horas} → Necesario: {resultado}")

        except ValueError as error:
            print(f"Pendiente: {horas} → ERROR: {error}")

def probar_duracion_compensacion():

    horas_pendientes = timedelta(hours=14, minutes=35)
    inicio = datetime(2026, 11, 28, 8, 0)

    fin = inicio + timedelta(hours=24)

    resultado = comprobar_duracion_compensacion(
        horas_pendientes,
        inicio,
        fin
    )

    print("\n--- PRUEBA DURACIÓN COMPENSACIÓN ---")
    print("Resultado:", resultado)

def probar_compensacion_invalida():

    pendiente = timedelta(hours=14, minutes=35)
    inicio = datetime(2026, 11, 28, 8, 0)
    limite = datetime(2026, 11, 30, 0, 0)

    # Caso 1: descanso insuficiente (20 horas)
    fin_insuficiente = inicio + timedelta(hours=20)

    resultado = comprobar_compensacion(
        pendiente, inicio, fin_insuficiente, limite
    )

    print("\n--- COMPENSACIÓN INSUFICIENTE ---")
    print("Resultado:", resultado)

    # Caso 2: compensación fuera de plazo
    inicio_tardio = datetime(2026, 11, 30, 8, 0)
    fin_tardio = inicio_tardio + timedelta(hours=24)

    resultado = comprobar_compensacion(
        pendiente, inicio_tardio, fin_tardio, limite
    )

    print("\n--- COMPENSACIÓN FUERA DE PLAZO ---")
    print("Resultado:", resultado)

def probar_registro_compensacion():

    inicio = datetime(2026, 11, 7, 18, 15)

    registro = registrar_compensacion(inicio, 30, 25)

    print("\n--- REGISTRO COMPENSACIÓN ---")

    for clave, valor in registro.items():
        print(f"{clave}: {valor}")

def probar_lista_compensaciones():

    compensaciones = []

    descansos = [
        (datetime(2026, 11, 7, 18, 15), 30, 25),
        (datetime(2026, 11, 21, 18, 0), 36, 0),
        (datetime(2026, 12, 5, 18, 0), 40, 0)
    ]

    for inicio, horas, minutos in descansos:

        registro = registrar_compensacion(
            inicio, horas, minutos
        )

        agregar_compensacion(compensaciones, registro)

    print("\n--- LISTA DE COMPENSACIONES ---")

    for registro in compensaciones:
        print(
            "Pendiente:", registro["horas_pendientes"],
            "| Límite:", registro["fecha_limite"],
            "| Estado:", registro["estado"]
        )

def probar_consulta_compensaciones():

    compensaciones = []

    descansos = [
        (datetime(2026, 11, 7, 18, 15), 30, 25),
        (datetime(2026, 11, 21, 18, 0), 36, 0),
        (datetime(2026, 12, 5, 18, 0), 40, 0)
    ]

    for inicio, horas, minutos in descansos:
        registro = registrar_compensacion(
            inicio, horas, minutos
        )
        agregar_compensacion(compensaciones, registro)

    fecha_consulta = datetime(2026, 12, 15, 12, 0)

    resultado = consultar_compensaciones(
        compensaciones, fecha_consulta
    )

    print("\n--- CONSULTA DE COMPENSACIONES ---")
    print("Pendientes:", resultado["cantidad_pendientes"])
    print("Horas pendientes:", resultado["horas_pendientes"])
    print("Vencidas:", resultado["cantidad_vencidas"])

    proxima = resultado["proximo_vencimiento"]

    if proxima is not None:
        print("Vencimiento más antiguo:", proxima["fecha_limite"])


def probar_estados_compensacion():

    registro = registrar_compensacion(
        datetime(2026, 11, 7, 18, 15),
        30,
        25
    )

    fechas = [
        datetime(2026, 11, 20),
        datetime(2026, 11, 28),
        datetime(2026, 12, 1)
    ]

    print("\n--- ESTADOS DE COMPENSACIÓN ---")

    for fecha in fechas:
        estado = obtener_estado_compensacion(registro, fecha)
        print(fecha.strftime("%d/%m/%Y"), ":", estado)



