from datetime import datetime, timedelta

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