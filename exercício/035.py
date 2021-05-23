#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep
import emoji
print('-=-'*20)
print('Analizandor de triângulos ')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('Analizando ⚙️⚙️⚙️')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('-=-' * 20)
    print('Os segmentos acima PODEM FORMAR triângulo! ')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('Os segmentos acima NÃO PODEM FORMAR triângulo! ')
    print('-=-'*20)
