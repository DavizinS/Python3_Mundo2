"""
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo
(Numero primo é Divisível por 1 ou por ele mesmo)
"""
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;35m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
if total == 2:
    print('\n\033[mO número {} é um número primo!'.format(num))
else:
    print('\n\033[mO numero {} não é primo!'.format(num))