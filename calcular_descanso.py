from datetime import datetime, timedelta

def calcular_descanso():

    descanso_reducido = 9
    descanso_normal = 11
    hora_actual = datetime.now()
    duracion = timedelta(hours=descanso_normal)
    fin_descanso = hora_actual + duracion
    duracion_r = timedelta(hours=descanso_reducido)
    fin_descanso_r = hora_actual + duracion_r
    

    print(hora_actual)
    print(fin_descanso)
    print(fin_descanso_r.strftime("%d/%m/%Y %H:%M"))

calcular_descanso()