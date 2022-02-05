grana = int(input('Qual valor deseja sacar? R$ '))
total = grana
cedula = 50
notas = 0
while True:
    if grana >= cedula:
        grana -= cedula
        notas += 1
    else:
        if notas > 0:
            print(f'Você recebeu {notas} de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        notas = 0
        if grana == 0:
            break
