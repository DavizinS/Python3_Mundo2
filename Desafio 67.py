"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    num = int(input('Você deseja ver a tabuada de qual número?: '))
    if num < 0:
        print('Você saiu... Volte sempre <3')
        break
    print('=' * 12)
    for c in range(1, 11):
        total = num * c
        print(f'{num} x {c} = {total}')
    print('=' * 12)
# Feito <3
