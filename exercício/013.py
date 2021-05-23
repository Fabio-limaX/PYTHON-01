#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Qual salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)

print(f'Um Funcionario que ganhava R${salário} com 15% de aumento, passar a receber R${novo} ')



