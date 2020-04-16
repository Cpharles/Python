"""Exercício Python 039:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo."""

from _datetime import date
anonasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - anonasc
print('Quem nasceu em {} tem {} anos em {}'.format(anonasc, idade, ano))
if idade < 18:
    n = 18 - idade
    n2 = ano + n
    print('Ainda faltam {} anos para o alistamento.'.format(n))
    print('Seu alistamento será em {}.'.format(n2))
elif idade > 18:
    n = idade - 18
    n2 = ano - n
    print('Você já deveria ter se alistado há {} anos.'.format(n))
    print('Seu alistamento deveria ter sido em {}.'.format(n2))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
