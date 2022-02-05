"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
(FEITO)
"""
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'roxo': '\033[1;35m', }

print('{}*={}'.format(cores['verde'], cores['limpa']) * 20)
print('{} NACIONAL BANK - EMPRESTIMOS {}'.format(cores['roxo'], cores['limpa']))
print('{}*={}'.format(cores['verde'], cores['limpa']) * 20)
casa = float(input('Qual o valor da Casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você consegue pagar? '))
prestacao = casa / (anos * 12)
minimo = (salario * 30 / 100)
print('\nPara pagar uma casa de {}R$ {:.2f}\033[m em {} anos'.format(cores['verde'], casa, anos))
print('\nO valor da prestação será de: {}R$ {:.2f}'.format(cores['verde'], prestacao))
if prestacao <= minimo:
    print('{}EMPRÉSTIMO CONCEDIDO!!'.format(cores['verde']))
else:
    print('{}EMPRÉSTIMO NEGADO!!'.format(cores['vermelho']))
