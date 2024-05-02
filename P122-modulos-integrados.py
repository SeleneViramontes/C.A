import os
import datetime, calendar

#Uso de algunas funciones del modulo: os

os.system("cls")
print("Sistema operativo", os.uname())
print("Carpeta actual   ", os.getcwd())
os.chdirt("/")
print(os.listdiri())
print("\nVariables de entorno :" , os.environ)
print("\nRuta :" , os.getenv("PATH"))

#Uso de alguns funciones del modulo: datetime 
ahora=datetime.datetime.now()
print("\nFecha y hora actuales", ahora)
print("\nLa fecha actual :", ahora.strftime("%b/ %d/ %Y"))
print("\nLa fecha actual :", ahora.strftime("%H:%M"))

#Uso de algunas funciones del modulo calendar 
print("\nCalendario Anual 2024:\n")
calendar.prcal(2024)
print("\nCalenario de un mes especifico")
calendar.prmonth (2024,4)