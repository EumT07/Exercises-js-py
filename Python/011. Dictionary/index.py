"""
Diccionarios de valores,son similares a los JSON en javascript, con claves y valores, se pueden modificar
"""
d = {}
print(type(d))


# key and value

colors = {
    "yellow": "amarillo",
    "blue": "azul",
    "green": "verde"
}

print(colors)
#Get any propierties
print(colors["blue"])

#in

result = "rojo" in colors #False
print(result)

#Delete
del(colors["green"])
print(colors)

#loops

# for --> show key
for color in colors:
    print(color)

# for --> key : value
for color in colors:
    print(color,colors[color])

# items
for key, value in colors.items():
    print(key, value)

#Methods

days = {
    "monday": "lunes",
    "tuesday": "martes",
    "Wednesday": "miercoles",
    "thursday":"jueves",
    "friday": "viernes",
    "saturday": "sabado",
    "sunday": "domingo"
}

# get(): find items
days_result_get = days.get("friday","Friday not exists")
print(days_result_get)

# pop(): Delete items
days_result_pop = days.pop("monday", "Monday doesn't exist")
print(days_result_pop)


#Getting keys
days_keys = days.keys()
print(days_keys)

#Gettings Values
days_values = days.values()
print(days_values)

#Gettin all items
days_items = days.items()
print(days_items)

print("\n Normal Loops")

#Loops
for day in days:
    print(day)

print("\n Keys ")

#Loops-Keys
for day in days.keys():
    print(day)

print("\n values ")

#Loops-values
for day in days.values():
    print(day)

print("\n items ")

#Loops-items
for day in days.items():
    print(day)


