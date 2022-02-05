"""
Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo
Será formado;
- Equilatero: Todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
r1 = float(input('Informe o segmento da 1° reta: '))
r2 = float(input('Informe o segmento da 2° reta: '))
r3 = float(input('Informe o segmento da 3° reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Poderá formar um TRIÂNGULO EQUILÁTERO!')  # Se os lados forem iguais
    elif r1 != r2 != r3 != r1:
        print('Poderá formar um TRIÂNGULO ESCALENO!')  # Se os lados forem diferentes
    else:
        print('Poderá formar um TRIANGULO ISOSCELES') # Lados iguais menos o ultimo
else:
    print('\033[1;31mNão foi possível formar um triângulo com os seguimentos indicados.')
