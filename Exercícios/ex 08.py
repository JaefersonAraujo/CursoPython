# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor: '))
cm = n * 100 # centímetros
mm = n * 1000 # milímetros

print(f"{n} metros é igual a {cm} centímetros e {mm} milímetros.")