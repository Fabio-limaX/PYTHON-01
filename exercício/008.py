#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))

medida1 = float(input('Uma distancia em metros: '))
cm1 = medida1 * 100
mm = medida1 * 1000

print(f'A medida de {medida}m corresponde a {cm}cm e {mm}mm ')

