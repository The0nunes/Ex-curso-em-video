# Crie um programa que faça o computador jogar Jokenpô com você.

import random

def jogar_jokenpo():
    nome_jogador = input('Digite seu nome para jogar: ')

    while True:
        escolha_jogador = input('Escolha: pedra, papel ou tesoura: ').lower()
        escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])

        print('-'*20)
        print(f'{nome_jogador} escolheu: {escolha_jogador}')
        print(f'O computador escolheu: {escolha_computador}')

        if escolha_jogador == escolha_computador:
            print('Empate!')
        elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
             (escolha_jogador == 'papel' and escolha_computador == 'pedra') or \
             (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
            print(f'{nome_jogador} ganhou!')
        else:
            print(f'{nome_jogador} perdeu!')

        print('-'*20)

        if input('Deseja jogar novamente? (s/n): ').lower() != 's':
            break


    print('Obrigado por jogar!')

if __name__ == '__main__':
    print('--- Bem-vindo ao Jogo de Jokenpo ---')
    jogar_jokenpo()
