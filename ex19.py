# O mesmo professor do desafio 18 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = []

for i in range(4):
    nome = input(f'Digite o nome do {i+1}º aluno: ')
    alunos.append(nome)

random.shuffle(alunos) # embaralha a ordem dos nomes

print('Ordem de apresentação dos trabalhos:')
for i, aluno in enumerate(alunos, 1):
    print(f'{i}. {aluno}')