# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

num_termos = 0

print('Os 10 primeiros termos da PA são:')
while num_termos < 10:
    termo_atual = primeiro_termo + num_termos * razao
    print(termo_atual, end=' ')
    num_termos += 1
