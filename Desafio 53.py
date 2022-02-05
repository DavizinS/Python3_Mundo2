"""
crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
Desconsiderando os espaços
Ex: Apos a sopa
ex2: A sacada da casa
ex: a torre da derrota
ex: o lobo ama o bolo
ex: anotaram a data da maratona

Anotações:
Então, eu vou ter que fazer com que o programa tire os espaços no caso vou usar o split
e assim vou ver se tem algo que faça a palavra reverter, e fazer uma condição
se a palavra revertida for igual a palavra digitada, então é uma palavra palíndromo.
"""
frase = str(input('Digite uma palavra: ')).strip().upper()
org = frase.split()
juntar = ''.join(org)
inverso = ''
for letra in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letra]
print('O inverso de {} é {}.'.format(juntar, inverso))
if juntar == inverso:
    print('É um Palíndromo!')
else:
    print('Não é um palíndromo!')
