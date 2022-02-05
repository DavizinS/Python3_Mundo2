"""
Melhore o jogo do desafio 028, onde o computador vai pensar em um número
entre 0 e 10. Só que agora o jogador vai adivinhar até acertar
mostrando no final quantos palpites foram necesários para vencer
(OK)
"""
from random import randint
palpites = 0
acerto = False
pc = randint(0, 10)
print('\033[1mDesafio \033[1;31m58\033[m ')
while not acerto:
    print('\033[1;34mAcabei de pensar em um número...\033[m\n')
    user = int(input('\033[1;35mEscolha um número de 0 a 10:  \033[m'))
    palpites += 1
    if user < pc:
        print('\033[1;34mMais... Tenta de novo.')
    else:
        print('\033[1;34mMenos... Tenta de novo...')
    if user == pc:
        acerto = True
print('\n\033[1;32mVocê adivinhou! Eu escolhi o número {}! '.format(pc))
print('\n\033[1;32mA quantidade de palpite até acertar foi exatamente {} vezes.'.format(palpites))
