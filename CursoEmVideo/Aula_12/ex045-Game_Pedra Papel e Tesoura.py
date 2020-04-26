"""Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você."""

i = 1
while i == 1:
    from random import randint
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = randint(0, 2) #sorteio do computador

    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')

    jogador = int(input('Qual a sua jogada? '))
    if jogador > 2:
        print('OPÇÃO INVALIDA')
        from sys import exit
        exit() #finaliza o programa

    from time import sleep
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO')
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)

    if computador == 0: #computador jogou PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
    elif computador == 1: #computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
    elif computador == 2: #computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCE')
        if jogador == 1:
            print('COMPUTADOR VENCE')
        if jogador == 2:
            print('EMPATE')
