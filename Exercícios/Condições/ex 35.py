# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Primeiro valor: "))
b = float(input("Segundo valor: "))
c = float(input("Terceiro valor: "))

if a + b > c and a + c > b and b + c > a:
    print("Pode formar um triângulo")
else:
    print("Não forma um triângulo ")