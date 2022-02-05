"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
no final do programa mostre
A média de idade do grupo
Qual o nome do homem mais velho
Quantas mulheres tem menos 20 anos.
"""
somaidade = 0
velhoidade = 0
menores = 0
nomev = ''
for c in range(1, 5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).strip()
    idade = int(input ('Qual a idade: '))
    sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()
    somaidade = somaidade + idade
    if idade > velhoidade and sexo == 'M':
        nomev = str(nome)
        velhoidade = idade
    if sexo == 'F' and idade < 20:
        menores = menores + 1
print('\033[1mA média de idade do Grupo é: {}.'.format(somaidade / 4))
print('O homem mais velho do Grupo tem {} anos e se chama: {}.'.format(velhoidade, nomev.title()))
print('No grupo existem {} mulheres abaixo de 20 anos.'.format(menores))
