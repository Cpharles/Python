"""Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('Qual é o salario do funcionério?:_'))
if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
print('O funcionário terá um aumento de R${:0.2f}'.format(aumento))
print('O valor do novo salário será de R${:0.2f}'.format(salario + aumento))
