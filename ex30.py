# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância em Km da sua viagem: '))

if distancia <= 200:
    preço_passagem = distancia * 0.50
    print(f'Preço a pagar: {preço_passagem}')
else:
    preço_passagem = distancia * 0.45
    print(f'Preço a pagar: {preço_passagem}')
