import datetime
from datetime import datetime

x1=int(input("Introduzca un valor de temperatura en grados centigrados:"))

x2=int(input("Introduzca un valor del porcentaje de humedad ambiente:"))

x3=str(input("Llovio, s \'o\' n:"))

if x3=="s":
   xb=True
elif x3=="n":   
   xb=False
else:
   print("Introduzca un valor valido (s o n)")
   raise ValueError("No se Guardo la Informacion de forma Correcta - Vuelva a correr el programa")   

now = datetime.now() # current date and time

#year = now.strftime("%Y")
#print("year:", year)

#month = now.strftime("%m")
#print("month:", month)

#day = now.strftime("%d")
#print("day:", day)

#time = now.strftime("%H:%M:%S")
#print("time:", time)

date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

print("Estos son los datos guardados  -","  Fecha:",date_time,"  Grados C:",x1,"  Porcentaje H:",x2,"  Llovio:",xb)

lineadatos = date_time + ',' + str(x1) + ',' + str(x2) + ',' + str(xb)

Datos = open('clase09_ej2Resuelto.csv', 'a')
Datos.write(lineadatos+'\n')
Datos.close()