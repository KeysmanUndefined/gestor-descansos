from datetime import datetime, timedelta
from motor.descanso_semanal import calcular_descanso_semanal_reducido

def calcular_limite_compensacion(inicio_descanso):

    inicio_semana = inicio_descanso.replace(
        hour=0, minute=0, second=0, microsecond=0
    ) - timedelta(days=inicio_descanso.weekday())

    limite = inicio_semana + timedelta(weeks=4)

    return limite

def calcular_descanso_necesario(horas_pendientes):

    if horas_pendientes <= timedelta(0):
        raise ValueError("Las horas pendientes deben ser positivas")

    descanso_minimo = timedelta(hours=9)

    return horas_pendientes + descanso_minimo

def comprobar_duracion_compensacion(
    horas_pendientes,
    inicio_descanso,
    fin_descanso
):
    if fin_descanso <= inicio_descanso:
        return "ERROR: fechas incoherentes"

    duracion = fin_descanso - inicio_descanso
    necesario = calcular_descanso_necesario(horas_pendientes)

    if duracion < necesario:
        return "INSUFICIENTE: faltan horas de descanso"

    return "CORRECTO: duración suficiente"

def comprobar_compensacion(
    horas_pendientes,
    inicio_compensacion,
    fin_compensacion,
    limite
):
    resultado = comprobar_duracion_compensacion(
        horas_pendientes,
        inicio_compensacion,
        fin_compensacion
    )

    if resultado != "CORRECTO: duración suficiente":
        return resultado

    if fin_compensacion > limite:
        return "FUERA DE PLAZO: compensación tardía"

    return "CORRECTO: duración y plazo de compensación"

def registrar_compensacion(inicio_descanso, horas, minutos=0):

    fin_descanso, horas_pendientes = calcular_descanso_semanal_reducido(
        inicio_descanso, horas, minutos
    )

    limite = calcular_limite_compensacion(inicio_descanso)

    compensacion = {
        "inicio_descanso": inicio_descanso,
        "fin_descanso": fin_descanso,
        "horas_pendientes": horas_pendientes,
        "fecha_limite": limite,
        "estado": "PENDIENTE"
    }

    return compensacion

def agregar_compensacion(lista_compensaciones, registro):

    lista_compensaciones.append(registro)

    return lista_compensaciones

def consultar_compensaciones(lista_compensaciones, fecha_actual):

    pendientes = []
    vencidas = []
    horas_totales = timedelta(0)

    for registro in lista_compensaciones:

        if registro["estado"] != "PENDIENTE":
            continue

        pendientes.append(registro)
        horas_totales += registro["horas_pendientes"]

        if fecha_actual >= registro["fecha_limite"]:
            vencidas.append(registro)

    proximo_vencimiento = min(
        pendientes,
        key=lambda registro: registro["fecha_limite"],
        default=None
    )

    return {
        "cantidad_pendientes": len(pendientes),
        "horas_pendientes": horas_totales,
        "cantidad_vencidas": len(vencidas),
        "proximo_vencimiento": proximo_vencimiento
    }

def obtener_estado_compensacion(registro, fecha_actual):

    if registro["estado"] == "COMPLETADA":
        return "COMPLETADA"

    if fecha_actual >= registro["fecha_limite"]:
        return "VENCIDA"

    tiempo_restante = registro["fecha_limite"] - fecha_actual

    if tiempo_restante <= timedelta(days=3):
        return "PROXIMO VENCIMIENTO"

    return "PENDIENTE"