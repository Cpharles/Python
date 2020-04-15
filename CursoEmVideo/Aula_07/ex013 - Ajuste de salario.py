'''
Escreva um algoritimo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento '''

SalAtual = float(input('Qual o salario do funcionário?_R$'))
SalNovo = SalAtual * 1.15
print('O novo salário com aumento de 15% é _ R${:0.2f}'.format(SalNovo))
