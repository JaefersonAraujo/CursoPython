# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um valor: "))
cont = 0
for c in range(2,num):
    if num % c == 0:
        cont += 1

if cont == 0:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")
    

