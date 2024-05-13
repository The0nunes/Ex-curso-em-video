# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

import math

def n_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        limite = math.isqrt(numero) + 1
        for i in range(3, limite, 2):
            if numero % i == 0:
                return False
        return True

numero = int(input('Digite um número inteiro: '))

if n_primo(numero):
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')
