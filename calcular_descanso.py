from datetime import datetime, timedelta

def calcular_descanso():

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



calcular_descanso()