#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

larg = float(input('Larguranda parede: '))
alt = float(input('Altura da parede: '))
área = larg + alt

tinta = área / 2

print(f'Sua parede tem a dimensão de: {larg}x{alt} e sua área é de {área}m² ')

print(f'Para pintar essa parede voce precisar de: {tinta}l de tinta')

