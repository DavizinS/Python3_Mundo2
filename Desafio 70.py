"""
Crie um programa que leia o nome e o preço de vários produtos
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

Nome do Produto:
Preço: R$
Quer continuar?

A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato.
"""
total = maiscaro = maisbarato = cont = 0
barato = ''
print('-' * 20)
print('Tech Info - Super Compras')
print('-' * 20)
while True:
    produto = str(input('Qual o nome do produto? ')).strip()
    preco = float(input('Qual o preço do produto? R$ '))
    cont += 1
    total = total + preco
    if preco >= 1000:
        maiscaro += 1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if resp == 'N':
        print('Você finalizou as compras.')
        break
print('{:~^40}'.format('FIM DAS COMPRAS'))
print(f'Produtos acima de R$ 1000: {maiscaro} produtos')
print(f'Produto mais barato foi {barato} e custa: R$ {maisbarato:.2f}')
print(f'A compra deu um Total de R$ {total:.2f}')
print('{:~^40}'.format('VOLTE SEMPRE! ^^'))
