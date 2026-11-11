from datetime import datetime, timedelta

def calcular_descanso_diario():

    descanso_reducido = 9
    descanso_normal = 11
    tipo_descanso = ""
    modo_calculo = ""
    hora_manual = ""
    fecha_convertida= ""
    
            
    while modo_calculo != "1" and modo_calculo != "2":
             modo_calculo = input("¿que quieres hacer? 1. calculo manual 2. calcular ahora  ")

    if modo_calculo == "1":
        fecha_manual = input("Introduce la fecha (DD/MM/AAAA): ")
        hora_manual = input("introduce la hora en formato 24h HH:mm    ")
        fecha_convertida = datetime.strptime(fecha_manual, "%d/%m/%Y")
        hora_convertida = datetime.strptime(hora_manual, "%H:%M")
        hora_inicio = datetime.combine(fecha_convertida.date(), hora_convertida.time())

    elif modo_calculo == "2":
        hora_inicio = datetime.now() 

    while tipo_descanso not in ("1", "2", "3"):
         tipo_descanso = input("¿Qué descanso quieres comprobar? 1. Normal 2. Reducido  3.Calcular fraccionado : ")
         

    if tipo_descanso == "1":         
         duracion = timedelta(hours = descanso_normal)
         fin_descanso = hora_inicio + duracion
         print(f"Tu descanso termina: {fin_descanso.strftime('%d/%m/%Y %H:%M')}")

    elif tipo_descanso == "2":
        duracion_r = timedelta(hours = descanso_reducido)
        fin_descanso_r = hora_inicio + duracion_r
        print(f"Tu descanso termina: {fin_descanso_r.strftime('%d/%m/%Y %H:%M')}")

    elif tipo_descanso == "3":
        limite_jornada = hora_inicio + timedelta(hours=15)
        print(
            f"Hora límite para iniciar las 9 horas de descanso: "
            f"{limite_jornada.strftime('%d/%m/%Y %H:%M')}"
        )

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

def calcular_limite_semanal(fin_descanso_anterior):
     limite = fin_descanso_anterior + timedelta(hours=144)
     return limite
     
#calcular_descanso_diario()
#fin_anterior = pedir_datos_semanal()
#limite = calcular_limite_semanal(fin_anterior)
#print(
    #f"Fecha y hora límite para iniciar el siguiente descanso semanal: "
   # f"{limite.strftime('%d/%m/%Y %H:%M')}"
#)


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

    
def calcular_descanso_semanal_reducido(inicio, horas, minutos=0):

    duracion = timedelta(hours=horas, minutes=minutos)

    if duracion < timedelta(hours=24) or duracion >= timedelta(hours=45):
        raise ValueError(
            "El descanso reducido debe ser de 24 a menos de 45 horas"
        )

    fin = inicio + duracion
    compensacion = timedelta(hours=45) - duracion

    return fin, compensacion


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

def probar_descanso_semanal_normal():

    fin_anterior = datetime(2026, 11, 5, 20, 0)
    inicio_nuevo = datetime(2026, 11, 11, 18, 0)

    limite = calcular_limite_semanal(fin_anterior)
    fin = calcular_descanso_semanal_normal(inicio_nuevo)
    resultado = comprobar_descanso_semanal(
        fin_anterior, inicio_nuevo
    )

    print("\n--- DESCANSO SEMANAL NORMAL ---")
    print("Límite:", limite)
    print("Finalización:", fin)
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


if __name__ == "__main__":
    probar_descanso_semanal_normal()
    probar_descanso_semanal_reducido()
    probar_calcular_descanso_necesario()
    probar_duracion_compensacion()
    probar_compensacion_invalida()
