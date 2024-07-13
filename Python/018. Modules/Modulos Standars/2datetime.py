import datetime
import locale

dt = datetime.datetime.now() 
print(dt)# 2022-04-19 15:45:02.812403
print(dt.year)# 2022
print(dt.month)# 04
print(dt.day)# 19
print(dt.hour)# 15 (3 pm)
print(dt.minute)# 45 m 
print(dt.second)# 02 segundos
print(dt.microsecond)# 812043 microsegundos


#Mostrar info de la hora formart

print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))
print(f"{dt.hour}:{dt.minute}:{dt.second}")

# Mostrar fecha con format

print(f"{dt.day}/{dt.month}/{dt.year}")

# Para crear una fecha

dt2 = datetime.datetime(2012,3,5)
print(dt2)# 2012-03-05

# reemplazar con replace

dt2 = dt2.replace(year=1980)
print(dt2)

# idoformat()

dt3 = datetime.datetime.now()

print(dt3)
print(dt3.isoformat())

# crear na cadena apartir de una fecha

"""
%A : Dia 
%d : fecha
%B : Mes
%I : Hora formato (normal)
%H : Hora formato (Militar)
%M : Minutos
"""
strDate = dt3.strftime("%A %d %B %Y %I:%M")
print(strDate)#Tuesday 19 April 2022 04:33


# Traducir 

locale.setlocale(locale.LC_ALL, "es")
strDate2 = dt3.strftime("%A %d %B %Y %I:%M")
print(strDate2)#martes 19 abril 2022 04:38

strDate3 = dt3.strftime("%A %d de %B del %Y -Hora: %H:%M")
print(strDate3)#martes 19 de abril del 2022 -Hora: 16:43

# Zonas horarias

"""
Descargar manualmente: pip3 install pytz

Time zone

luego import pytz

pytz.all_timezones --> mostrara todas las zonas horarias


horaTokio = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
horaTokio.strftime("%A %d %B %Y %I:%M")
"""






