# Crie um programa que leia o nome completo de uma pessoa e mostre: – O nome com todas as letras maiúsculas e
# minúsculas. – Quantas letras ao todo (sem considerar espaços). – Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
quantidade_letras = len(nome)
nome_sem_espacos = nome.replace(' ', '')
quantidade_letras = len(nome_sem_espacos)
primeiro_nome = nome.split()[0]  
quantidade_letras_primeiro_nome = len(primeiro_nome)

print(f'Nome em maiúsculas: {nome_maiusculo}')
print(f'Nome em minúsculo: {nome_minusculo}')
print(f'Quantidade de letras ao todo: {quantidade_letras}')
print(f'Quantidade de letras do primeiro nome: {quantidade_letras_primeiro_nome}')

