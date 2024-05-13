# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input('Digite uma frase: ').replace(' ', '').upper()

frase_invertida = frase[::-1].upper()

if frase == frase_invertida:
    print(f'A FRASE DIGITADA FOI: {frase} \nE A FRASE DE TRÁS PARA FRENTE É: {frase_invertida}')
    print(f'É UM PALÍNDROMO')
else:
    print(f'A FRASE DIGITADA FOI: {frase} \nE A FRASE DE TRÁS PARA FRENTE É: {frase_invertida}')
    print(f'NÃO É UM PALÍNDROMO')
