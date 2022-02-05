from time import sleep
resp = 0
maior = 0
n1 = int(input('\033[1;34mDigite o 1° valor: '))
n2 = int(input('Digite o 2° valor: \033[m'))
while resp != 5:
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print("""
    \033[1;34m[1] Somar
    \033[1;35m[2] Multiplicar
    \033[1;36m[3] Maior
    \033[1;33m[4] Novos números
    \033[1;31m[5] Sair do Programa\033[m
    """)
    resp = int(input('\033[1mDigite uma opção:\033[m '))
    if resp == 1:
        print('\n\033[1mSoma: {} + {} = {}\033[m'.format(n1, n2, n1 + n2))
    if resp == 2:
        print('\n\033[1;34mMultiplicação: {} x {} = {}.\033[m'.format(n1, n2, n1 * n2))
    if resp == 3:
        print('\033[1;34mO maior valor digitado foi: {}\033[m'.format(maior))
    if resp == 4:
        print('\033[1;34mVoltando a escolha de número...\033[m')
        sleep(1)
        n1 = int(input('\033[1;34mDigite o 1° valor: '))
        n2 = int(input('\033[1;34mDigite o 2° valor: \033[m'))
    if resp == 5:
        print('\033[1;31mSaindo...')
        sleep(1)
        print('\033[1;31mAguarde mais um pouco...\033[m')
        sleep(1.5)
        print('\033[1;31mVocê saiu do programa.')
    if resp > 5:
        print('\033[1;31mComando Inválido! Tente novamente.\033[m')
