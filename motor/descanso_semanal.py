from datetime import datetime, timedelta

def calcular_limite_semanal(fin_descanso_anterior):
     limite = fin_descanso_anterior + timedelta(hours=144)
     return limite

def calcular_descanso_semanal_normal(inicio_descanso):
    duracion = timedelta(hours=45)
    fin_descanso = inicio_descanso + duracion

    return fin_descanso

def comprobar_descanso_semanal(fin_anterior, inicio_nuevo):

    limite = calcular_limite_semanal(fin_anterior)

    if inicio_nuevo < fin_anterior:
        return "ERROR: las fechas no son coherentes"

    elif inicio_nuevo > limite:
        return "FUERA DE PLAZO: superadas las 144 horas"

    else:
        return "CORRECTO: descanso iniciado dentro del plazo"