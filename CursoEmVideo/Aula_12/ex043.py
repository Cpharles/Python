"""Exercício Python 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

peso = float(input('Qual é a sua peso? [kg]:_'))
altura = float(input('Qual é o seu altura? [mt]:_'))
icm = peso / (altura ** 2)
print('Seu Índice de Massa Corporla (IMC) é de: {:0.1f}'.format(icm))
if icm < 18.5:
    print('Você esta ABAIXO DO PESO!')
elif 18.5 < icm <= 25:
    print('Você esta com o PESO IDEAL!')
elif 25 < icm <= 30:
    print('Você esta com SOBREPESO!')
elif 30 < icm <= 40:
    print('Você esta com OBESIDADE!')
elif icm > 40:
    print('Você esta com OBESIDADE MORBIDADE!')


