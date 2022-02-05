"""
Crie um programa que leia duas notas de um aluno e calcule sua média
mostrando uma mensagem no final, de acordo com a média atingida
- Media abaixo de 5.0
REPROVADO
- Média entre 5.0 e 6,9
Recuperação
- Média superior a 7.0
APROVADO
"""
n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[1;31mVocê foi reprovado!')
elif media <= 6.99:
    print('\033[1;35mVocê está de recuperação!')
else:
    print('\033[1;32mVocê foi aprovado!')
print('\033[1;mSua média foi {:.1f}'.format(media))
