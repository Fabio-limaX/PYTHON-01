# Condições Alinhadas

nome = str(input('Qual é seu nome? '))
if nome == 'Felipe':
    print('Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Enzo':
    print('Seu nome é bem popular no Brasil. ')
elif nome == 'Ana Claúdia Jésica Juliana':
    print('Belo nome femenino! ')
else:
    print('Seu nome é bem normal. ')
print(f'Tenha um bom dia, {nome}')
