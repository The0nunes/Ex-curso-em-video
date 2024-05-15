# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

import random

print('--- Tente adivinhar um número entre 0 a 10 ---')
numero_pensado = random.randint(0, 10)
palpites = 0

while True:
    numero = int(input('Digite um número de 0 a 10: '))
    palpites += 1
    
    if numero < 0 or numero > 10:
        print('O número digitado não está no intervalo desejado!')
    else:
        if numero == numero_pensado:
            print(f'Parabéns você acertou em {palpites} palpites!')
            break
        else:
            print('Você errou, tente outra vez!')

