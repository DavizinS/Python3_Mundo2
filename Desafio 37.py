"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""
num = int(input('Digite um número: '))
print('\033[1;33m=*\033[m' * 20)
print('Calculadora Binária')
print('\033[1;33m=*\033[m' * 20)
print('''
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal
''')
resp = int(input('Digite sua opção de acordo com os números: '))
if resp == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif resp == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif resp == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mComando inválido!')