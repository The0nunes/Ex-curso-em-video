'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''

altura_pessoa = float(input('Altura (ex.: 1.70): '))
peso_pessoa = float(input('Peso (ex.: 69.2): '))

calculo_imc = (peso_pessoa) / pow(altura_pessoa, 2)

if calculo_imc < 18.5:
    print(f'SEU IMC: {calculo_imc:.2f} - ABAIXO DO PESO')
elif calculo_imc >= 18.5 and calculo_imc <= 25:
    print(f'SEU IMC: {calculo_imc:.2f} - PESO IDEAL')
elif calculo_imc > 25 and calculo_imc <= 30:
    print(f'SEU IMC: {calculo_imc:.2f} - SOBREPESO')
elif calculo_imc > 30 and calculo_imc <= 40:
    print(f'SEU IMC: {calculo_imc:.2f} - OBESIDADE')
else:
    print(f'SEU IMC: {calculo_imc:.2f} - OBESIDADE MÓRBIDA')
