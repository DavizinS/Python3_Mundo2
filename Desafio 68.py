"""
Faça um programa que jogue par ou impar com o computador.
O jogo so será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo.
"""
from random import randint
cont = 0
escolha = ''
total = 0
print('=' * 20)
print('IMPAR OU PAR?')
print('=' * 20)
while True:
    num = int(input('Escolha um numero: '))
    while True:
        escolha = str(input('Par ou Ímpar[P/I]? ')).strip().lower()[0]
        if escolha == 'p':
            print('Você escolheu PAR.')
            break
        if escolha == 'i':
            print('Você escolheu IMPAR.')
            break
        else:
            ''
    pc = randint(0, 10)
    total = num + pc
    if escolha == 'p':
        if total % 2 == 0:
            print('Você ganhou.')
            print(f'Você escolheu {num} e o Computador escolheu {pc}. O total é: {total}, e é PAR!')
            cont += 1
            print('-' * 20)
        else:
            print('Você perdeu.')
            print(f'Você escolheu {num} e o Computador escolheu {pc}. O total é {total}, e é IMPAR!')
            break
    if escolha == 'i':
        if total % 2 == 1:
            print('Você Ganhou.')
            print(f'Você escolheu {num} e o Computador escolheu {pc}. O total é: {total}, e é ÍMPAR!')
            print('-' * 20)
            cont += 1
        else:
            print('Você perdeu.')
            print(f'Você escolheu {num} e o Computador escolheu {pc}. O total é {total}, e é PAR!')
            break
print(f'GAME OVER... Você venceu {cont} vezes.')
# Feito
