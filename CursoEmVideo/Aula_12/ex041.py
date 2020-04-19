"""Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta:_'))
idade = date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))
print('Classificação: ', end='')
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
