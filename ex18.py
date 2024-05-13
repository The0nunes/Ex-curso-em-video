# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

nomes_alunos = []

while True:
    nomes = input('Digite o nome do aluno: ')

    nomes_alunos.append(nomes)
    escolher_aluno = random.choice(nomes_alunos)

    entrada = input('Tem mais alunos para escolher?: ')
    if entrada.lower() == 'nao':
        print(f'O aluno escolhido foi: {escolher_aluno}')
        break

