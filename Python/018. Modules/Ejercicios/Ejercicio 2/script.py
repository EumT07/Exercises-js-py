"""
Desarrollar un reloj que de hora, minutos y segudos, con la hora actual.

Sleep(segundos: Permite pausar el reloj durante un tiempo, el modulo os de la funcions system("cls") o system("clear"))

"""
import datetime
import time
import os

while True:
    os.system("cls")
    timeNow = datetime.datetime.now()
    print(f"Son las: {timeNow.hour}:{timeNow.minute}:{timeNow.second}")
    time.sleep(1)




