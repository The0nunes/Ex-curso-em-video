# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

def forma_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

lado1 = float(input('Digite o comprimento da primeira reta: '))
lado2 = float(input('Digite o comprimento da segunda reta: '))
lado3 = float(input('Digite o comprimento da terceira reta: '))

if forma_triangulo(lado1, lado2, lado3):
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
