# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import random

print('--- Tente adivinhar um número entre 0 a 5 ---')
numero = int(input('Digite um número de 0 a 5: '))

numero_pensado = random.randint(0, 5)

if numero < 0 or numero > 5:
    print('O número digitado não está no intervalo desejado!')
else:
    if numero == numero_pensado:
        print('Parabéns você acertou!')
    else:
        print('Você errou, tente outra vez!')

