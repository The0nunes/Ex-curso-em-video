# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida: – Média abaixo de 5.0: REPROVADO – Média entre 5.0 e 6.9: RECUPERAÇÃO 
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Média {media} = Aprovado')
elif media >= 5:
    print(f'Média {media} = Recuperação')
else:
    print(f'Média {media} = Reprovado')
