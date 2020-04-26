"""Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valcasa = float(input('Informe o valor da casa:_'))
salario = float(input('Informe o valor do salário do comprador:_'))
anospag = int(input('Informe a quantidade de anos desejado para financiar a casa:_'))
parcela = int(valcasa / (anospag * 12))
metrica = salario * 0.3
print('Para comprar uma casa de R${:0.2f} em {} anos a prestação será de R${:0.2f}'.format(valcasa, anospag, parcela))
if parcela >= metrica:
    print('Infelizmente o valor da prestação compromete mais de 30% do seu salário')
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo pode ser APROVADO!')
