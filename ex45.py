# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

import time

def contagem_regressiva_for(tempo):
    for i in range(tempo, 0, -1):
        print(i)
        time.sleep(1)
    print('Fogos estourando!')

tempo1 = 10
contagem_regressiva_for(tempo1)

# OU 

def contagem_regressiva_while(tempo):
    while tempo > 0:
        print(tempo)
        time.sleep(1)
        tempo -= 1
    print('Fogos estourando!')

tempo2 = 10
contagem_regressiva_while(tempo2)
