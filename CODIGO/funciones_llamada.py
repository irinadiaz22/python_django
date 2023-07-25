"""
Formas de llamar a una función en Python
"""

def sumar(a,b):
    return a+b

# 1 posicional:
print(sumar(1,2))

# 2 nominal
print(sumar(b=2, a=1))

# 3 con una tupla
t = (1,2)
print(sumar(t[0],t[1]))
print(sumar(*t))

# 4 con un dict:
d = {"a":1, "b":2}
print(sumar(**d))

