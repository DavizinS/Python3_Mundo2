"""
Faça um programa que leia o ano de nascimento de um jovem e informe
de acodo com sua idade
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta uo passou do prazo
(OK)
"""
from datetime import date
nasc = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - nasc
tempo = abs(18 - idade)
if idade < 17:
    print('\033[1;31mVocê tem {} anos, e ainda falta {} anos para você se alistar!\033[m'.format(idade, tempo))
elif idade == 17 or idade == 18:
    print('Você tem {} anos!'.format(idade))
    print('\033[1;31mVocê já pode se alistar! Vá até uma Junta Militar mais próxima da sua casa!\033[m')
elif idade < 45:
    print('Você tem {} anos'.format(idade))
    print('\033[1;35mSe ainda não se alistou vá se alistar pois já está {} anos atrasado!\033[m'.format(tempo))
    print('\033[1;33mSeu ano de alistamento foi {}\033[m'.format(anoatual - tempo))
else:
    print('Você passou da idade de alistamento! Se ainda não se alistou, você foi dispensado!')
    print('Vá até uma junta militar e faça o registro do seu \033[1;32mReservista\033[m!')
