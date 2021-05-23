#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Estar em maiusculo? ', a.isupper())
print('Estar em minusculo? ', a.islower())
print('Estar capitalizada? ', a.istitle())

a = input('Digite algo: ')

print(f'o tipo primitivo desse valor é: {type(a)}')
print(f'Só tem espaço? {a.isspace()}')
print(f'É um numero? {a.isnumeric()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Estar em maiusculo? {a.isupper()}')
print(f'Estar em ninusculo? {a.islower()}')
print(f'Estar capitalizado? {a.istitle()}')
