#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

"""
import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))


from math import trunc
num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e sua porção inteira é {trunc(num)}')
"""

num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e sua porção inteira é {int(num)} ')
