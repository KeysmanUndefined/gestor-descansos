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
from test.test_descansos import (
    probar_descanso_semanal_normal,
    probar_descanso_semanal_reducido,
)
from test.test_compensaciones import (
    probar_calcular_descanso_necesario,
    probar_duracion_compensacion,
    probar_compensacion_invalida,
    probar_registro_compensacion,
    probar_lista_compensaciones,
    probar_consulta_compensaciones,
    probar_estados_compensacion,
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
     
#calcular_descanso_diario()
#fin_anterior = pedir_datos_semanal()
#limite = calcular_limite_semanal(fin_anterior)
#print(
    #f"Fecha y hora límite para iniciar el siguiente descanso semanal: "
   # f"{limite.strftime('%d/%m/%Y %H:%M')}"
#)
























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
