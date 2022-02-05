"""
Crie um prorama que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar...
Se o usuário uer ou não continuar. No final mostre

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas Muiéres tem menos de 20 anos.
"""
maiores = homem = mul = 0
while True:
    print('-' * 20)
    print('Cadastro de Pessoas')
    print('-' * 20)
    idade = int(input('Qual a idade da pessoa? '))
    if idade >= 18:
        maiores += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Qual o sexo[M/F]? ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade < 20:
            mul += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        print('Você parou o REGISTRO.')
        break
print(f'Ao total foram {maiores} pessoas maiores de 18 anos, {homem} homens e {mul} mulheres com menos de 20 anos.')
# Feito
