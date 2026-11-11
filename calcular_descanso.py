from datetime import datetime, timedelta

from motor.descanso_diario import calcular_descanso_diario

from motor.descanso_semanal import (
    calcular_limite_semanal,
    calcular_descanso_semanal_normal,
    comprobar_descanso_semanal,
    calcular_descanso_semanal_reducido,
)

from motor.compensaciones import (
    calcular_limite_compensacion,
    calcular_descanso_necesario,
    comprobar_duracion_compensacion,
    comprobar_compensacion,
    registrar_compensacion,
    agregar_compensacion,
    consultar_compensaciones,
    obtener_estado_compensacion,
)

from test.test_descansos import probar_descanso_semanal_normal


def pedir_datos_semanal():
    fecha_manual = input("Introduce la fecha fin del descanso anterior (DD/MM/AAAA): ")
    hora_manual = input("Introduce la hora fin del descanso anterior(HH:MM): ")

    fecha_convertida = datetime.strptime(fecha_manual, "%d/%m/%Y")
    hora_convertida = datetime.strptime(hora_manual, "%H:%M")

    hora_inicio = datetime.combine(
        fecha_convertida.date(),
        hora_convertida.time()
    )

    return hora_inicio
     
#calcular_descanso_diario()
#fin_anterior = pedir_datos_semanal()
#limite = calcular_limite_semanal(fin_anterior)
#print(
    #f"Fecha y hora límite para iniciar el siguiente descanso semanal: "
   # f"{limite.strftime('%d/%m/%Y %H:%M')}"
#)











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


def probar_descanso_semanal_reducido():

    inicio = datetime(2026, 11, 7, 18, 15)

    fin, compensacion = calcular_descanso_semanal_reducido(
        inicio, 30, 25
    )

    limite = calcular_limite_compensacion(inicio)

    print("\n--- DESCANSO SEMANAL REDUCIDO ---")
    print("Inicio:", inicio)
    print("Fin:", fin)
    print("Compensación:", compensacion)
    print("Límite compensación:", limite)

    # PRUEBA DE COMPENSACIÓN

    inicio_compensacion = datetime(2026, 11, 28, 8, 0)
    fin_compensacion = datetime(2026, 11, 29, 8, 0)

    resultado = comprobar_compensacion(
        compensacion,
        inicio_compensacion,
        fin_compensacion,
        limite
    )

    print("\n--- COMPROBACIÓN COMPENSACIÓN ---")
    print("Inicio:", inicio_compensacion)
    print("Fin:", fin_compensacion)
    print("Duración:", fin_compensacion - inicio_compensacion)
    print("Resultado:", resultado)


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


if __name__ == "__main__":
    probar_descanso_semanal_normal()
    probar_descanso_semanal_reducido()
    probar_calcular_descanso_necesario()
    probar_duracion_compensacion()
    probar_compensacion_invalida()
    probar_registro_compensacion()
    probar_lista_compensaciones()
    probar_consulta_compensaciones()
    probar_estados_compensacion()
