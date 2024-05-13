# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

def decimal_para_binario(numero):
    return bin(numero)[2:]

def decimal_para_octal(numero):
    return oct(numero)[2:]

def decimal_para_hexadecimal(numero):
    return hex(numero)[2:]

numero = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'O número {numero} em binário é: {decimal_para_binario(numero)}')
elif opcao == 2:
    print(f'O número {numero} em octal é: {decimal_para_octal(numero)}')
elif opcao == 3:
    print(f'O número {numero} em hexadecimal é: {decimal_para_hexadecimal(numero)}')
else:
    print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
