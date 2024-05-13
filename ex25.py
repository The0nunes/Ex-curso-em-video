# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição
# ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite qualquer frase: ').upper()

quantidade_a = frase.count('A')
primeira_posicao = frase.find('A')
ultima_posicao = frase.rfind('A')

print(f'Quantidade de "A": {quantidade_a}')
print(f'Posição da primeira ocorrência: {primeira_posicao}')
print(f'Posição da última ocorrência:: {ultima_posicao}')
