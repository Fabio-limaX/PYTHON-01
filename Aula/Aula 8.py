#Exemplo da aula

#(import bebida) 'Vai importa todas as bebidas '(import math)

#(from doce import podim) 'Vai importa as funciolanidades que eu escolher'(from math import sqrt)

"""
math: significa matematica
caeil:faz um arredondamento para cima
floor:faz um arredondamento para baixo
trunc:vai eliminar da , para frente
pow:potencia
sqrt:calcular raiz quadrada
factorial
"""


import math
import emoji as emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')
