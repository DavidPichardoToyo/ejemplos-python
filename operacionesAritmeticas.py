import math as m
import pandas as pd




"""# operaciones aritmeticas
# Suma
print(3 + 3)
# Resta
print(3 - 3)
# Multiplicación
print(3 * 3)
# Divisiones
print(3 / 3)
# Potencias
print(3 ** 3)
# modulo
print(3 % 3)
# division de flotantes
print(3 // 4)

#
# Tipos de datos
#

print(type(10))
print(type(3.14))
print(type(1 + 3j))
print(type("texto"))
print(type([1,2,3,4,5,6,[1,2,3,4,5,6,7,8,9]]))
print(type((93,4,5,6,7,8,3)))
print(type({'nombre':'David'}))
print(type(3 > 2))
print(type({1,2,3,4,5,6,7,8,9,1}))

list = [1,2,3,4,5,6,[1,2,3,4,5,6,7,8,9]]
print(len(list))

name = "juan"
print(len(name))

"""
# area de un triangulo
#A = (√3 /4) * a²

"""lado = float(input(" longitud del lado del triangulo?"))
area = (m.sqrt(3) / 4) * lado ** 2

print(f"Area del triangulo es : {area:.1f}")
"""

#area de un anillo
#Area =  π * ( R**2 – r**2 )

"""R = float(input("radio mayor : "))
r = float(input("radio menor : "))
area = m.pi * (R**2 - r**2)

print(f"el area de anillo es de : {area:.1f}")
"""
df = pd.read_csv('clash_royale_cards.csv')

print("las primeras 5 filas de mi csv")
print(df.head())