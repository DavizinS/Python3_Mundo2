"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER
"""
from datetime import date
anoatual = date.today().year
nasc = int(input('Em qual ano você nasceu? '))
idade = anoatual - nasc
print('O atleta tem \033[1;36m{}\033[m anos'.format(idade))
if idade <= 9:
    print('Classificação: \033[1;36mMIRIM.')
elif idade <= 14:
    print('\033[mClassificação: \033[1;34mINFANTIL.')
elif idade <= 19:
    print('\033[mClassificação: \033[1;35mJUNIOR.')
elif idade <= 25:
    print('\033[mClassificação \033[1;33mSENIOR.')
else:
    print('\033[mClassificação \033[1;31mMASTER.')