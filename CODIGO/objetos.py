"""
Pruebas con POO
"""

class Persona():
    """
    Implementación de la clase Persona
    """
    apellido = "Sanz"

    def __init__(self, nombre="",edad=0, altura=0.0):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura

    def cumple(self):
        self.edad += 1

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)
    
    def __repr__(self):
        return str(self)

p1 = Persona("Eva",45, 1.8)
p2 = Persona("Sandra",25, 1.7)
L = [p1, p2, Persona("Jorge", 33, 1.8)]
print(L)
for p in L:
    print(p)
exit()

print(p1)
p1.cumple()
print(p1)
p2.cumple()
print(p2)
print(p2.apellido)
print(p1.apellido)
p1.apellido="Gomez"
print(p2.apellido)
print(p1.apellido)
print(Persona.apellido)
p1.telefono = 600450540
print(p2.__dict__)
print(p1.__dict__)


"""
print(str(p1))
print(p1.__str__())
print(p1.nombre)
"""

