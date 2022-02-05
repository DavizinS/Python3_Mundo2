"""
Exercício Python 66:
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
soma = cont = 0
print('*=' * 20)
print('Desafio 66 - Curso em Video')
print('*=' * 20)
while True:
    n = int(input('\nDigite um número[\033[1m999 para parar]: \033[m '))
    if n == 999:
        break
    cont += 1
    soma = soma + n
print(f'Fora digitados {cont} valores, e a soma deles é: {soma}')
# Feito
