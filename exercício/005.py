#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um numero: '))
a = n - 1
s = n + 1
print('Analizando seu valor: {}, seu antecessor é: {} e o sucessor é: {}'.format(n, a, s))

#Outra forma em baixo

n = int(input('Digite um numero: '))

print('Analizando seu valor: {}, Seu antecessor é: {} e o sucessor é: {}'.format(n, (n-1), (n+2)))

print(f'Analizando seu valor: {n}, seu antecessor é: {n-1} e o sucessor é: {n+1}')
