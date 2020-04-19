"""Exercício Python 044:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
Considere as opçºoes de escolha para definir o valor a ser mostrado
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

print("{:=^40}".format(' LOJAS GUANABARA '))
valProduto = float(input('Qual o valor da compra: R$'))
print('''FORMAS DE PAGAMENTOS:
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    Avista = valProduto - (valProduto * 0.1)
    print('Sua compra de R${:0.2f} sair à vista por R${:0.2f}'.format(valProduto, Avista))
    print('Desconto de 10%')
elif op == 2:
    cartao = valProduto - (valProduto * 0.05)
    print('Sua compra de R${:0.2f} vai sair no cartão por R${:0.2f}'.format(valProduto, cartao))
    print('Desconto de 5%')
elif op == 3:
    parcela2 = valProduto / 2
    print('Sua compra de R${:0.2f} será parcelado em 2x de R${:0.2f}'.format(valProduto, parcela2))
    print('Não tem desconto, é o valor da compra')
elif op == 4:
    Nparcela = int(input('Quantas parcelas? '))
    parcelaX = (valProduto + (valProduto * 0.2)) / Nparcela
    total = parcelaX * Nparcela
    print('Sua compra será parcela em {}x de R${:0.2f} com juros de 20%'.format(Nparcela, parcelaX))
    print('Sua compra de R${:0.2f} após o pagamento das parcelas vai sair por R${:0.2f}'.format(valProduto, total))
