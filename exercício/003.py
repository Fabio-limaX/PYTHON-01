#Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2

print('A soma entre {:.2f} e {:.2f} é igual a {:.2f}!'.format(n1, n2, s ))


n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))

s = n1 + n2

print(f'A soma entre {n1 :.2f} e {n2 :.2f} é igual a {s :.2f}!')
