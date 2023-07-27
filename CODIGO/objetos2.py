"""
Implementación de una clase Hora con el operador +
"""

class Hora:
    """
    Implementación clase Hora para operaciones de tipo
    h=2, m=5  --> 02:05
    h=16, m=15 -> 16:15
    2:5
    """
    def __init__(self, h=0, m=0):
        self.h = h
        self.m = m

    def __str__(self):
        return "%02d:%02d" % (self.h, self.m)
    
    def __add__(self, otro):
        horas = self.h+otro.h
        minutos = self.m+otro.m
        aux_h = minutos // 60
        horas += aux_h
        minutos %= 60
        return Hora(horas, minutos)
    
class Fecha:

    def __init__(self, dd=1,mm=1,yy=1970):
        self.dd=dd
        self.mm=mm
        self.yy=yy

    def __str__(self):
        return "%02d/%02d/%04d" % (self.dd, self.mm, self.yy)
    
class FechaHora(Hora, Fecha):
    
    def __init__(self, dd=1, mm=1, yy=1970, h=0, m=0):
        Fecha.__init__(self, dd, mm, yy)
        Hora.__init__(self, h, m)

    def __str__(self):
        return Fecha.__str__(self) + " " + Hora.__str__(self)
    
h1 = Hora(16,15)
print(h1)
h2 = Hora(2,55)
print(h2)
suma = h1 + h2 # Busca el método especial __add__
print(suma)
hoy = Fecha(27,7,2023)
print(hoy)
ahora = FechaHora(27,7,2023,17,2)
print(ahora)

    