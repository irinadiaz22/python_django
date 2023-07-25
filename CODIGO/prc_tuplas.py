"""
Función partition: viene bien para ficheros windows
"""
import os

#fichero = "libro1.xlsx"
fichero = "listas.py"
t = fichero.partition('.')
print(t)
print('La extensión del fichero es: ', t[2])

archivos = os.listdir('../doc')
extensiones = ('txt','py','pdf')
for f in archivos:
    t = f.partition('.')
    if t[2] in extensiones:
        print(f)
