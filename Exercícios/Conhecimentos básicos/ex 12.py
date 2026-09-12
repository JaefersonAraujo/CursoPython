# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("Qual o preço do produto? ")) # preço
d = (p * 5) / 100 # desconto
np = p - d # novo preço

print(f"O valor do produto é R$ {p:.2f} com 5% de desconto ficará por R$ {np:.2f}")


