"""Faça um programa que calcule a soma entre todos os numeros impares
que são múltipos de três e que se encontram no intervalo de 1 até 500"""
s = 0
cont = 0
for c in range(1, 500+1):
    if c % 3 == 0:
        if c % 2 == 1:
            cont += 1
            s += c
print('FIM.')
print('A soma dos {} valores solicitados, é igual a: \033[1;36m{}.'.format(cont, s))