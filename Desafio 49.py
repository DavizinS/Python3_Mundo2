"""
Refaça o desafio 009.
Mostrando a tabuada de um número que o usuário escolher
só que agora utilizando o laço 'for'
"""
mul = int(input('Você deseja ver a \033[1;32mTabuada\033[m de qual número? '))
for c in range(1, 10+1):
    resul = mul * c
    print('\033[1;32m{} x {} = \033[1;34m{}'.format(mul, c, resul))
print('\n\033[1mFim da Tabuada.')
