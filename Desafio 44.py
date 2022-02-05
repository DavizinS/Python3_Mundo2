"""
Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu: preço normal, e condição de pagamento
- A vista dinheiro cheque: 10% de desconto
- á vista no cartão: 5% de desconto
- em até 2x no cartão preço normal
- 3x ou mais no cartão 20% de juros
(FEITO OK)
"""
print('\033[1m-=' * 20)
print('\033[1;31mLOJAS AMERICANAS\033[m')
print('\033[1m-=\033[m' * 20)
preco = float(input('Digite o valor do produto: R$ '))
avista = preco - (preco * 10 / 100)  # Desconto de 10 %
avistac = preco - (preco * 5 / 100)  # Desconto de 5 %
p2 = preco  # Preço Normal
p3 = preco + (preco * 20 / 100)
print('\033[1;32m-=\033[m' * 20)
print('Qual o método de pagamento? ')
print('\033[1;32m-=\033[m' * 20)
print('[1] Dinheiro: A Vista\n[2] Cartão: A Vista\n[3] Cartão: Em Até 2x!\n[4] Cartão: Em Até 3x')
resp = str(input('Escolha de acordo com o número:  '))
if resp == '1':
    print('Você escolheu o método: DINHEIRO A VISTA.')
    print('O valor do produto é R$ {:.2f} e com desconto de 10% foi para R$ {:.2f}'.format(preco, avista))
elif resp == '2':
    print('Você escolheu o método: CARTÃO A VISTA.')
    print('O valor do produto é R$ {:.2f} e com desconto de 5% foi para R$ {:.2f}'.format(preco, avistac))
elif resp == '3':
    print('Você escolheu o método: PARCELADO EM ATÉ 2x.')
    print('O valor das parcelas é 2x de R$ {:.2f}.'.format(preco / 2))
elif resp == '4':
    parcelas = int(input('Quantas parcelas? '))
    print('Você escolheu o método: PARCELADO EM {}x .'.format(parcelas))
    print('O valor do produto terá um ajuste de 20% de juros! O valor do produto é R$ {:.2f}!'.format(p3))
    print('O valor das parcelas é {}x de R$ {:.2f}'.format(parcelas, p3 / parcelas))
else:
    print('\033[1;31mComando inválido! Tente novamente.')
