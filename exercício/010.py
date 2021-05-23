#

real = float(input('Quanto voce tem na carteira? '))

dolar = real / 5.44
euro = real / 6.44

print('Com: R${:.2f}, você pode comprar: UR${:.2f}, e: EUR${:.2f} '.format(real, dolar, euro ))


real = float(input('Quanto você tem na carteira? '))

dolar = real / 5.44
euro = real / 6.44

print(f'Com: R${real :.2f}, você pode compar: UR${dolar :.2f}, e EUR${euro :.2f}')
