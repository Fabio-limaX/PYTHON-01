"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal """

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÀRIO
[ 2 ] Converter paras OCTAL 
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÀRIO é igual a {bin(num)[2:]} ')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]} ')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida Tente novamente.')

# COM .format ABAIXO

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÀRIO
[ 2 ] Converter paras OCTAL 
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÀRIO é igual a {} '.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num, hex(num)[2:]))
else:
    print('Opção inválida Tente novamente.')