#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é menor ')
elif n2 > n1:
    print('O SEGUNDO valor é maior ')
else:
    print('Os dois valores são IGUAIS! ')

