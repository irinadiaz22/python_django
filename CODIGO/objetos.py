"""
Pruebas con POO
"""

class Persona():
    """
    Implementación de la clase Persona
    """
    contador=0

    def __init__(self, nombre="",edad=0, altura=0.0):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        Persona.contador += 1

    def cumple(self):
        self.edad += 1

    def hablar(self, otro=None):
        if not otro:
            print(self.nombre,'habla solo')
        else:
            print(self.nombre,'y',otro.nombre,'están hablando')

    def __str__(self):
        return self.nombre + " " + str(self.edad) + " " + str(self.altura)
    
    def __repr__(self):
        return str(self)
    
    def __del__(self):
        print('Se elimina: ', self.nombre)
        Persona.contador -= 1

class Guia(Persona):

    def __init__(self, nombre="", edad=0, altura=0, ambito='', idiomas=[]):
        #super().__init__(nombre, edad, altura)
        Persona.__init__(self, nombre, edad, altura)

        self.ambito = ambito
        self.idiomas = idiomas

    def __str__(self):
        return Persona.__str__(self)+ " "+self.ambito + " " + \
        ",".join(self.idiomas)
    
    def hablar(self, otro=None):
        pass

def testGuia():
    g1 = Guia('Pedro',34, 1.77, 'N', ['inglés','Francés'])
    g2 = Guia('Sara',44, 1.79, 'I', ['inglés','Alemán'])
    print(g1)
    g1.cumple()
    print(g1)
    g1.hablar(g2)


def testPersona():
    print("Num personas: ", Persona.contador)
    p1 = Persona("Eva",45, 1.8)
    p2 = Persona("Sandra",25, 1.7)
    p3 = Persona("Jose",25, 1.7)
    print("Num personas: ", Persona.contador)
    L = [p1, p2, Persona("Jorge", 33, 1.8)]
    print("Num personas: ", Persona.contador)
    del(p3)
    print("Num personas: ", Persona.contador)

    print(L)
    for p in L:
        print(p)
    p1.hablar()
    p2.hablar(p1)

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

testGuia()