# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome Completo: ')).strip()
nome = n.split()
print(f'Muito Prazer em te Conhecer! {n} ')
print(f'Seu primeiro nome é {nome[0]}')
print(f'seu último nome é {nome[len(nome)-1]} ')
