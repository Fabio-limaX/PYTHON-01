#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))

media = (n1 + n2) / 2
print('A média entre {:.1f} e {} é igual a {:.1f} '.format(n1, n2, media))


n3 = float(input('Primeira nota do aluno: '))
n4 = float(input('Segunda nota do aluno: '))

média = (n1 + n2) / 2
print(f'A média entre {n3 :.1f} e {n4 :.1f} é igual a {média :.1f}')
