"""
Importar de septuptools; para poder crear nuestro paquete distribuible

"""
from setuptools import setup

setup(
    name="download",
    version="0.0.1",
    description="Primer paquete de distribucion",
    author="Eublan Mata",
    author_email="eublanmata@gmail.com",
    url="http://eublanmata.com",
    scripts=[],# *Buscar info*
    packages=["paquete","paquete.A","paquete.B"]
)

"""
*La carpeta origen debe estar en escritorio para realizar una buena creacion

Para crearlo escribimos lo siguiente:

python setup.py sdist --> dentro de cmd cn el path de la carpeta
sdist: crear una ditribuible

Una vez ya creado, Nos va salir un archivo winrar, o con el comprimidor de preferencia de su dispositivo, luego ingresamos a la carpeta, y mediante la consola introducimos este comando:

Instalar: 
            pip3 install "name of packages"

Desintalar:
            pip3 unistall download

Una vez realizado eso podemos visualisar que se instalo en nuestro sistema python con el siguiente comando:
            pip3 list

"""