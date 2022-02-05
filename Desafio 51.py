"""
Desenvolva um programa que leia o primeiro termo e a razão
de uma PA(Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão.
"""
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao  # Formula da PA
for c in range(termo, decimo + razao, razao):
    print('-> {}'.format(c), end=' ')
print('-> FIM <-')
