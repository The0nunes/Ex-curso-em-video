# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = float(input('Qual a velocidade do carro? '))

if velocidade_carro > 80:
    valor_multa = (velocidade_carro - 80) * 7
    print(f'VOCÊ FOI MULTADO! Valor da multa: R${valor_multa:.2f}')
else:
    print('Velocidade normal')
