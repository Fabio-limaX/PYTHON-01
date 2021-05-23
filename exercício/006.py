#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))

# \n serve para deixar as coisa uma embaixo da outra

n1 = int(input('Digite um numero: '))
d1 = n * 2
t1 = n * 3
r1 = n ** (1/2)
print(f'O dobro de {n1} vale {d1} ')
print(f'O triplo de {n1} vale {t1}. \n A raiz quadrada de {n1} é igual a {r1 :.2f}')
