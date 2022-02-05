"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: obesidade
- Acima de 40: Obesidade mórbida
(FEITO OK)
"""
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[1;36mVOCÊ ESTÁ ABAIXO DO PESO!')
elif imc <= 25:
    print('\033[1;32mVOCÊ ESTÁ NO PESO IDEAL!')
elif imc <= 30:
    print('\033[1;33mVOCÊ ESTÁ NO SOBREPESO!')
elif imc <= 40:
    print('\033[1;35mVOCÊ ESTÁ NA OBESIDADE!')
else:
    print('\033[1;31mVOCÊ ESTÁ NA OBESIDADE MÓRBIDA! CLASSE DE RISCO!')
