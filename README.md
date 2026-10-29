# Gestor de descansos

Programa en Python para calcular a qué hora puedo volver a conducir después de realizar un descanso diario.

La idea es ir añadiendo funciones poco a poco, mientras aprendo Python, hasta poder comprobar también los descansos semanales y bisemanales.

El objetivo final es **poder utilizarlo desde mi móvil Android**, de forma sencilla. Pulsar un botón al terminar la jornada y que el programa calcule automáticamente los descansos, sin tener que introducir fechas ni horas manualmente.

## Primera versión

De momento el programa:

- Obtiene la fecha y hora actuales.
- Calcula cuándo terminan las 11 horas de descanso normal.
- Calcula cuándo terminan las 9 horas de descanso reducido.
- Muestra los resultados por pantalla.

## Prueba de funcionamiento

![Resultado del programa](captura_descansos.png)

## Próximos pasos

- Comprobar cuándo se puede utilizar un descanso reducido.
- Calcular los descansos semanales normales y reducidos.
- Controlar las compensaciones y los descansos entre semanas.
- Comprobar los cálculos según la normativa vigente.
- Crear una interfaz sencilla para utilizarlo en Android.

Por ahora solo calcula las horas. Todavía no comprueba si se cumplen todos los requisitos legales.

## Actualización — 29/10/2026

### Nuevas funcionalidades

- Introducción manual de fecha y hora de inicio de jornada.
- Posibilidad de calcular desde la fecha y hora actuales.
- Cálculo de descansos diarios normales de 11 horas.
- Cálculo de descansos diarios reducidos de 9 horas.
- Cálculo de la hora límite para iniciar un descanso de 9 horas dentro del período de 24 horas desde el final del descanso anterior.

### Cálculo del límite de 15 horas

Para determinar la última hora a la que debe comenzar un descanso de 9 horas:

```python
limite_jornada = hora_inicio + timedelta(hours=15)
```

Ejemplo:

```text
Inicio de jornada: 07:00
Hora límite para iniciar 9 horas de descanso: 22:00
```

Este cálculo también sirve para el segundo período de un descanso diario fraccionado de 3 + 9 horas, siempre que se hayan realizado previamente las primeras 3 horas ininterrumpidas.

**Limitación:** el programa calcula el límite horario, pero todavía no verifica el cumplimiento completo de la normativa, las pausas ni los tiempos de conducción.

### Conceptos de Python aprendidos

**1. `datetime.now()`**

Obtener la fecha y hora actuales.

```python
hora_actual = datetime.now()
```

**2. `datetime.strptime()`**

Convertir una cadena de texto en un objeto `datetime`.

```python
fecha = datetime.strptime("29/10/2026", "%d/%m/%Y")
hora = datetime.strptime("07:00", "%H:%M")
```

**3. `datetime.combine()`**

Combinar una fecha y una hora.

```python
hora_inicio = datetime.combine(fecha.date(), hora.time())
```

**4. `timedelta()`**

Representar una duración y realizar cálculos con fechas y horas.

```python
fin_descanso = hora_inicio + timedelta(hours=11)
```

**5. Validación de opciones con `while` y `not in`**

```python
while tipo_descanso not in ("1", "2", "3"):
    tipo_descanso = input("Selecciona una opción: ")
```

Permite repetir la pregunta hasta recibir una opción válida.

**6. Formatear fechas con `strftime()`**

```python
print(fin_descanso.strftime("%d/%m/%Y %H:%M"))
```

**7. Análisis estático con Ruff**

Instalación:

```bash
python -m pip install ruff
```

Comprobar el código:

```bash
python -m ruff check calcular_descanso.py
```

Aplicar formato:

```bash
python -m ruff format calcular_descanso.py
```

Aprendizaje: Ruff puede detectar variables declaradas pero no utilizadas, además de otros problemas de calidad del código. Sus advertencias deben revisarse antes de aplicar correcciones automáticas.



### Próximas mejoras

- Validación de entradas incorrectas.
- Comprobación completa del descanso fraccionado de 3 + 9 horas.
- Pruebas automatizadas con `assert`.
- Control de descansos diarios reducidos.
- Gestión de cambios de horario de verano e invierno.

### Referencia normativa

Reglamento (CE) 561/2006, artículos 4 y 8.
