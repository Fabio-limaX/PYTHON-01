"""Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo."""

#Forma sem o (FROM)
import math
ángulo = float(input('Digite um angulo que você deseja: '))
seno = math.sin(math.radians(ángulo))
print(f'O ángulo de {ángulo} tem o SENO de {seno :.2f}')
cosseno = math.cos(math.radians(ángulo))
print(f'O ángulo de {ángulo} tem o COSSENO de {cosseno :.2f}')
tangente = math.tan(math.radians(ángulo))
print(f'O ángulo de {ángulo} tem a TANGENTE de {tangente :.2f} ')

#Forma com o (FROM)

from  math import radians, sin, cos, tan
ángulo = float(input('Digite um angulo que você deseja: '))
seno = sin(radians(ángulo))
print(f'O ángulo de {ángulo} tem o SENO de {seno :.2f}')
cosseno = cos(radians(ángulo))
print(f'O ángulo de {ángulo} tem o COSSENO de {cosseno :.2f}')
tangente = tan(radians(ángulo))
print(f'O ángulo de {ángulo} tem a TANGENTE de {tangente :.2f} ')
