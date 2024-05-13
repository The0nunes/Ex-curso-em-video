# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Digite seu nome: ')

nome_dividido = nome.split()
sobrenome = nome_dividido[-1]

if sobrenome.lower() == 'silva':
    print('Tem "SILVA" no nome')
else:
    print('Não tem "SILVA" no nome')
