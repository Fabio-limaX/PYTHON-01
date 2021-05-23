
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem! ')
else:
    print('Seu nome é tão normal! ')
print(f'Bom dia, {nome} ')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua media foi boa! PARABÉNS!')
else:
    print('Sua média foi orriveu! ESTUDE BEM MAIS!')

       # Ou condição simplificada

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m}')
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')
