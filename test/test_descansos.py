from datetime import datetime, timedelta

from motor.descanso_semanal import (
    calcular_limite_semanal,
    calcular_descanso_semanal_normal,
    comprobar_descanso_semanal,
    calcular_descanso_semanal_reducido,
)

from motor.compensaciones import (
    calcular_limite_compensacion,
    comprobar_compensacion,
)

def probar_descanso_semanal_normal():

    fin_anterior = datetime(2026, 11, 5, 20, 0)
    inicio_nuevo = datetime(2026, 11, 11, 18, 0)

    limite = calcular_limite_semanal(fin_anterior)
    fin = calcular_descanso_semanal_normal(inicio_nuevo)
    resultado = comprobar_descanso_semanal(
        fin_anterior, inicio_nuevo
    )

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


