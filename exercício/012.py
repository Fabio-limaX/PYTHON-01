#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto R$'))
novo = (preço * (5 / 100)) + preço

print('O produto que custava {:.2f}, na promoção de 5% vai custa R${:.2f} '.format(preço, novo))


preço = float(input('Qual é o preço do produto R$'))
novo = (preço * (5 / 100)) + preço

print(f'O produto que custava {preço :.2f}, na promoção de 5% vai custa R${novo :.2f}')
