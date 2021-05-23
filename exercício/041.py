#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação; MIRIM ')
elif idade <= 14:
    print('Classificação: INFANTIL ')
elif idade <= 19:
    print('Classificação: JUNIOR  ')
elif idade <= 25:
    print('Classificação: SÊNIOR ')
else:
    print('Classificação: MASTER ')
