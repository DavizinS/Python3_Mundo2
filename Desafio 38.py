""""
Escreva um programa que leia dois números inteiros e compare-os
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais
(Feito)
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('\033[1;34mO primeiro valor é maior! Pois {} é maior que {}.\033[m'.format(n1, n2))
elif n2 > n1:
    print('\033[1;35mO segundo valor é maior! Pois {} é maior que {}.\033[m'.format(n1, n2))
else:
    print('\033[1;35mOs números digitados são iguais!\033[m')
