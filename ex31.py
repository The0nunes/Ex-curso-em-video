# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o ano a ser verificado: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O {ano} é um ano bissexto')
else:
    print(f'O {ano} não é um ano bissexto')
