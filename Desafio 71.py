"""
Crie um programa que simule o funcionamento de um caixa eletronico
No inicio pergunte ao usuário qual será o valor a ser sacado
Numero inteiro) e o progrma vai informar quantas cedulas de cada valor
serão entregues

Considere que o caixa possui cedulas de R$50, R$20, R$ 10 e R$1

Que valor você quer sacar? R$
Total de cedulas de 50
total de celulas de 20
total de cedulas de 10
Total de cedulas de 1
"""
grana = int(input('Quantos R$ você deseja sacar? '))  # quanto eu desejo sacar..
total = grana  # Grana vai se converter ao total
cedula = 50  # Cedula atual
totcedula = 0  # Quantas cedulas eu tenho.
while True:  # Loop Infinito
    if grana >= cedula:  # Se meu dinheiro for maior que a cedula atual! Tipo Se 100 for maior que 50!
        grana -= cedula  #Então, Meus 100 vai ser tirado por 50(Que é a nota atual)
        totcedula += 1  # E aqui vai me dar uma cedula! Que começando é 50!(Se tiver mais que 50 é claro, volta a tirar)
    else:  # Senão ...
        if totcedula > 0:  # Se meu total de cedula for maior que 0
            print(f'Você recebeu {totcedula} cédulas de R$ {cedula}')  # Vai digitar aqui, as cédulas.
        if cedula == 50:  # Se a cedula for de 50, no caso se eu não tiver mais de 50..
            cedula = 20  # A cédula de 50, vira, cedula de 20.
        elif cedula == 20:  # Senão, se não tiver mais de 20, a cedula muda
            cedula = 10  # E de 20, vira a cedula de 10.
        elif cedula == 10:  # Se não tiver mais 10
            cedula = 1  # A cedula de 10, vira de 1 R$
        totcedula = 0  ## E No final O do loop, as cedulas zeram.. Pois elas já foram escritas, ali em cima.
        if grana == 0:  # Aqui se a grana for 0, irá pausar
            break  # Break. Pausou.
