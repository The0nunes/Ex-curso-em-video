# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_rodados = float(input(f'Quantos Km foram rodados com o carro? '))
dias_alugados = float(input(f'Quantos dias o carro foi alugado? '))

preco_total = (km_rodados * 0.15) + (dias_alugados * 60)

print(f'O preço total a se pagar é de R${preco_total}')
