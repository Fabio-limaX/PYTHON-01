

print('Categoria: FATIAMENTO cortar a frase! ')

frase = 'Curso em Video Python'

print('Frase [9]')
print('Frase [9:13] Significa: Fatiando com o numero exato letra do ultimo número vai ignorada! ')
print('Frase [9:21] Significa: colocando um numero a mais a frase vai ser fatiada corretamente! ')
print('Frase [9:21:2] Significa: Colocando :2 vai fatiar pulando de 2 em 2 letras! ')
print('Frase [:5] Significa: Começar do inicio e vai terminar no número digitado! ')
print('Frase [15:] Significa: Que eu sei o inicio mais não sei o final! ')
print('Frase [9::3] Significa: Vai pular de 3 em 3 letras! ')

print('Categoria: ANALISE saber informacões da frase! ')

frase = 'Curso em Video Python'

print("len(frase) Significa: Comprimento da frase! ") #Importante
print("frase.count('o') Significa: Contagem de deteminada letra! ")
print("frase.count('o', 0, 13) Significa: Contagem ja com fatiamento! ")
print("frase.find('deo') Significa: Quataas vezes ele encontrou (EX: deo)! ")
print("frase.find('Android') Significa: Verificar se existe taó palavra,/"
      " se não tiver vai retornar -1 significando que não existe! ")
print("'Curso' in frase Significa: Verifica se existe 'curso' na frase, vai me retornar True ou False! ")

print('Categoria: TRANSFOMACÃO ')

print("frase.replace('Python', 'Android') Significa: Vai encontrar a palavra e vai substituir a palavra!  ")
print("frase.upper() Significa: Que as letras vão ficar em maiúsculas! ")
print("frase.lawer() Significa: Que as letras vão ficar em minúsculas! ")
print("frase.capitalize() Significa: Vai deixar todas as outras letras em minúsculas só a primeira letra da fica maiúscula! ")
print("frase.title() Significa: Vai deixar o inicio de todas as string em maiúscula! ")
print("frase.strip() Significa: Vai remover todos os espaços inuteis no inicio é no final! ")
print("frase.rstrip() Significa: Vai remover só os ultimos espaços da string! ")
print("frase.lstrip() Significa: Vai remover só os primeiros espaços da string!  ")

print("Categoria: Divição e Juncão  ")

print("frase.split() Significa: Vai dividir a string em uma lista de números! ")
print(" '-'.join(frase) [junção] Significado:Vai juntar todos os elemntos de frase nesse separador '-' ")


#Exemplos:

frase = 'Curso em Video Python'
print(frase[:13])
