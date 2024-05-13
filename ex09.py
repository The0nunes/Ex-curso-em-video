# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro_carteira = float(input('Quanto dinheiro você tem? '))

cotação_dolar = 5.12

conversao = dinheiro_carteira / cotação_dolar

print(f'Com {dinheiro_carteira} reais você consegue comprar {conversao:.2f} dolares')
