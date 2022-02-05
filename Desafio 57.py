"""
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor
correto
"""
"""while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo [M/F]? ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Não reconhecido! Digite o seu Sexo novamente! [M/F]: '))
if sexo == 'M':
    sexoo = 'Masculino'
if sexo == 'F':
    sexoo = 'Feminino'
print('Cadastro Feito com Sucesso! Sexo: {}.'.format(sexoo))
"""
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'Mmff':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
