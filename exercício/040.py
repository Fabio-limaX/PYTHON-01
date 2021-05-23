#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1 :.1f} e {nota2 :.1f}, a média do aluno é {média :.1f}')
if média >=5 and média < 7:
    print('O aluno está em RECUPERAÇÂO. ')
elif média < 5:
    print('o aluno está REPROVADO. ')
elif média >= 7:
    print('O aluno está APROVADO. ')
