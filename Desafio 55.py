"""
Faça um programa que leia o peso de 5 pessoas
e no final mostre qual foi o maior e o menor peso lidos
"""
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[1;31mO mais pesado informado foi: {:.2f}kg'.format(maior))
print('\033[1;32mO menos pesado informado foi: {:.2f}kg'.format(menor))
