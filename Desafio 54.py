"""
Crie um programa que leia o ano de nascimento de 7 pessoas
no final mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maioridade
"""
from datetime import date
maiores = 0
menores = 0
atual = date.today().year
for c in range(1, 8):
    idade = int(input('Em qual ano a {}° pessoa nasceu? '.format(c)))
    idade2 = atual - idade
    if idade2 < 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('\033[1mCom base nas idades informadas temos: ', end='')
print('{} pessoas que já atingiram a maioridade\nE são {} pessoas que ainda não são de maior.'.format(maiores, menores))
