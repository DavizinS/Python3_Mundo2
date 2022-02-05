"""
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, se não for desconsidere
"""
soma = 0
pares = 0
for c in range(1, 6+1):
    num = int(input('Escolha o {}° número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        pares += 1
print('Ao total foram \033[1;35m{}\033[m numeros pares'.format(pares))
print('A soma dos números pares é de: \033[1;33m{}'.format(soma))
