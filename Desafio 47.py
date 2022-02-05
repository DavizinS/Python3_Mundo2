"""Crie um programa que mostre na tela
todos os números pares que estão no intervalo de 1 a 50"""
from time import sleep
print('\033[1;31mContagem de números Pares\033[m')
for c in range(2, 51, 2):
    print('\033[1;30m-> \033[1;31m{}\033[m \033[1;30m<-'.format(c), end='')
    sleep(0.3)
print('\n\033[1;39mFIM.')