#Concatenacion con .format()

ho = "joder"

print("{:>30}".format("Hello")) #30 caracteres a la derecha(alineacion)
print("{:30}".format("word"))#Izquierda
print("{:^30}".format("word"))#centro

print("{:^30}".format(ho))#centro
print("{:.3}".format(ho))#Truncamiento

print(f"{ho:.4}")# Truncamiento

# format con numeros
print("{:04d}".format(20))
print("{:4d}".format(200))
print("{:4d}".format(2000))

#f con numeros
n1 = 100
print(f"{n1:4d}")

# rellenar con ceros
print(f"{n1:04d}")

#mostrar decimales
pi = 3.145469

print(f"{pi:.3f}")
# rellenar con espacios
print(f"{pi:7.3f}")
# rellenar con ceros
print(f"{pi:07.3f}")