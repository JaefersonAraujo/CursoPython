# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

op = float(input("Qual o comprimento do cateto oposto? ")) # cateto oposto
ad = float(input("Qual o comprimento da cateto adjacente? ")) # cateto adjacente

hi = hypot(op,ad)

'''soma = (op ** 2 + ad ** 2) 
raiz = soma ** (0.5) # ou soma ** (1/2)


print(f"A soma dos catetos é {soma}, o comprimento total da hipotenusa é de {raiz:.2f}")'''

print(f"A hipotenusa vai medir {hi:.2f}")



