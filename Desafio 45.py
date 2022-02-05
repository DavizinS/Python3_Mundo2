"""
Crie um programa quefaça o computador jogar Jokenpô com você (FEITO OK)
"""
from random import choice
from time import sleep
print('\033[1;32m-=\033[m' * 20)
print('\033[1;33mJokenpô - V1.0 (Davidbrr)\033[m')
print('\033[1;32m-=\033[m' * 20)
jogo = ['PEDRA', 'PAPEL', 'TESOURA']
user = str(input('Escolha: Pedra, Papel ou Tesoura? ')).strip().upper()
pc = choice(jogo)
print('\n\033[1;36mJo\033[m')
sleep(0.6)
print('\033[1;36mKen\033[m')
sleep(0.6)
print('\033[1;36mPô\033[m\n')
if user == 'PEDRA' and pc == 'TESOURA':
    print('\033[1;32mVocê ganhou!')
elif user == 'TESOURA' and pc == 'PAPEL':
    print('\033[1;32mVocê ganhou!!')
elif user == 'PAPEL' and pc == 'PEDRA':
    print('\033[1;32mVocê ganhou!!')
elif user == 'TESOURA' and pc == 'PEDRA':
    print('\033[1;31mVocê perdeu! Tenta de novo kkkk.')
elif user == 'PEDRA' and pc == 'PAPEL':
    print('\033[1;31mVocê perdeu! Tenta de novo kkkk.')
elif user == 'PAPEL' and pc == 'TESOURA':
    print('\033[1;31mVocê perdeu! Tenta de novo kkkk.')
elif user != 'PEDRA' and user != 'PAPEL' and user != 'TESOURA':
    print('\033[1;31mVOCÊ DIGITOU O COMANDO ERRADO...\033[m')
else:
    print('\033[1;34mEmpatamos!')
print('Eu escolhi {} e você escolheu {}'.format(pc, user))
