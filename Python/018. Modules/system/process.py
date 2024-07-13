import subprocess

#Mostrar en shell
# subprocess.run(["ls", "-la"], shell=True)


#Capturar Stdout
# p1 = subprocess.run(["ls","-la"], capture_output=True)
#print(p1.args)
# print(p1.stdout.decode())


#Decode --> convertir in string
# p1 = subprocess.run(["ls","-la"], capture_output=True)
# print(p1.stdout.decode())


#Si no queremos usar decode, colocamos text=True
# p1 = subprocess.run(["ls","-la"], capture_output=True, text=True)
# print(p1.stdout)


#Usando stdout=subprocess.pipe
# p1 = subprocess.run(["ls","-la"], stdout=subprocess.PIPE, text=True)
# print(p1.stdout)

#Creando un file
# with open("output.txt", "w") as f:
#     p1 = subprocess.run(["ls","-la"], stdout=f, text=True)


#stderr -> obteniendo un error
# with open("output.txt", "w") as f:
#     p1 = subprocess.run(["ls","-la", "dne"], capture_output=True, text=True, check=True)
# print(p1.stderr)


#CAT --> obtener info de un file 
p1 = subprocess.run(["cat", "test.txt"], capture_output=True, text=True)


#GREP --> write
p2 = subprocess.run(["grep", "-n", "python"], 
capture_output=True, text=True, input=p1.stdout)

print(p2.stdout)







