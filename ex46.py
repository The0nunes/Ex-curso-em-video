# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

def contagem_pares():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)

contagem_pares()