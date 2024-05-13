# Refaça o DESAFIO 8, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite qualquer numero: '))

for i in range(0, 11):
    print(f'{n} x {i} = {n * i}')
