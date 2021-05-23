#Exercício Python 20:
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1,  n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)

#Usando o from!!

from random import shuffle
n5 = str(input('Primeiro aluno: '))
n6 = str(input('Segundo aluno: '))
n7 = str(input('Terceiro aluno: '))
n8 = str(input(('Qusrto aluno: ')))
lista = [n5, n6, n7, n8]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
