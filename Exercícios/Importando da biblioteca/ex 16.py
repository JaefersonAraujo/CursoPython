# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''from math import trunc # usando método importando da biblioteca
num = float(input("Digite um valor: "))

print(f"O valor digitado foi {num} e sua porção inteira é {trunc(num)}.")'''

num = float(input("Digite um valor: ")) # utilizando a função int 

print(f"O valor digitado foi {num} e sua porção inteira é {int(num)}")
