#Ejercicio 4
import datetime

horaAgregar = 2

horaActual = datetime.datetime.now()

horaSuma = datetime.timedelta(hours=horaAgregar)

horaTotal = horaSuma+horaActual

print(horaTotal.time())