"""Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

nota1 = float(input('Primeira nota:_'))
nota2 = float(input('Segunda nota:_'))
media = (nota1 +nota2) / 2
nota = round(media, 1)
print('Sua média é de {:0.1f}'.format(media))
if media < 5:
    print('REPROVADO!')
elif media >= 5 or media <= 6.9:
    print('RECUPERAÇÃO')
elif media > 6.9 or media >= 7:
    print('APROVADO')
