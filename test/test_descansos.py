from datetime import datetime, timedelta

from motor.descanso_semanal import (
    calcular_limite_semanal,
    calcular_descanso_semanal_normal,
    comprobar_descanso_semanal,
)

def probar_descanso_semanal_normal():

    fin_anterior = datetime(2026, 11, 5, 20, 0)
    inicio_nuevo = datetime(2026, 11, 11, 18, 0)

    limite = calcular_limite_semanal(fin_anterior)
    fin = calcular_descanso_semanal_normal(inicio_nuevo)
    resultado = comprobar_descanso_semanal(
        fin_anterior, inicio_nuevo
    )
