"""Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa."""

# Sem importação do (math)

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'hipotenusa vai adiar {hi :.2f}')

#Com a importação do math

import math
co2 = float(input('Comprimento do cateto oposto: '))
ca2 = float(input('Comprimento do cateto adiacente: '))
hi2 = math.hypot(co2, ca2)
print(f'A hipotenusa vai medir {hi}')


from math import hypot
co3 = float(input('Comprimento do cateto oposto: '))
ca3 = float(input('Comprimento do cateto adiacente: '))
hi3 = hypot(co3, ca3)
