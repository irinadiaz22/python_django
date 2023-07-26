"""
Pruebas con POO
"""

class Persona():
    """
    Implementación de la clase Persona
    """

    def __init__(self, nombre="",edad=0, altura=0.0):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)

p1 = Persona("Eva",45, 1.8)
print(p1)
print(str(p1))
print(p1.__str__())

