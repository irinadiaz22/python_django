"""
Diccionarios en python. Crear, recorrer, acceso a elementos

"""

d = {"uno":1, "dos":2, "tres":3}
d['cuatro']=4
d['uno']=1000
print(d, type(d))

d = {"nombre":"Alberto","edad":45,"altura":1.78}
print(d['nombre'])

datos = {"5188800": {"nombre":"Alberto","edad":45,"altura":1.78}}
print(datos['5188800']['nombre'])
datos['5188800']['nombre'] = 'Eva'
print(datos)


L = [1,2,3,4,5]
s = "adios"
d = dict(zip(L, s))
print(d)
d = dict(zip(s, L))
print(d)

# Datos de un alumno: nombre, asignatura y notas
alumno = {"nombre":"Miguel","asignatura":"Excel", "notas":[7.8,4.5,9.9,3]}
# imprimir la ultima:
print(alumno["notas"][-1])
