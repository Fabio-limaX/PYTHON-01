# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

distância = float(input('Qual é a distâcia da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}Km. ')
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print(f'e o preço da sua passagem será de R${preço :.2f}')

# Forma Simplificada

distância = float(input('Qual é a distâcia da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}Km. ')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'e o preço da sua passagem será de R${preço :.2f}')
