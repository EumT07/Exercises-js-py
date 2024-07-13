import os
import datetime
#getcwd --> path
# print(os.getcwd())

#chdir --> move back == cd..
os.chdir("/Users/EumT07/Desktop/")
# print(os.getcwd())


#listdir -->  ls para ver que hay en el directorio; carpetas archivos
# print(os.listdir())

#Crear carpetas


#mkdir --> crear carpeta simple
# os.mkdir("img2")
#os.mkdir("img2/mh") #Cuando existe si puede crearla
# os.mkdir("img6/mh") #Cuando no existe, lanza un error

#makedirs --> crea carpeta y permite crearle contenido
# os.makedirs("im3/family")

#Remove

# os.rmdir("im2")
# os.removedirs("im2")

#rename
# os.rename("img2", "images")

#stat
# mod_tmime = os.stat("test.txt").st_mtime
# print(datetime.datetime.fromtimestamp(mod_tmime))


#walk --> Va caminar o buscar dentro de cada carpeta, va a encontrar los files, carpetas siempre y cuando indiques la dirrecion

# for dirpath, dirnames, filenames in os.walk("C:/Users/EumT07/Desktop/TEST CODE"):
#     print("current Path:", dirpath)
#     print("Directories:", dirnames)
#     print("Files:", filenames)
#     print()

#Acces any locations
#HOMEPATH --> windows
# print(os.environ.get('HOMEPATH'))#\Users\EumT07

#Concatenar files
# file_path = os.path.join(os.environ.get("HOMEPATH"), "test1.txt")
# print(file_path)

# #basename
# print("basename: ",os.path.basename("/tmp/test.txt"))
# #dirname
# print("dirname: ",os.path.dirname("/tmp/test.txt"))
# #Split
# print("split: ", os.path.split("/tmp/test.txt"))
# #existe
# print("Exist: ", os.path.exists("/tmp/test.txt"))

#Encontrar un files y si extension
# print("splitext: ", os.path.splitext("/tmp/test.txt"))

#path
print(dir(os.path))







