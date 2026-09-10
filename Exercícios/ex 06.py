# Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite valor: '))
d = n * 2 # dobro
t = n * 3 # triplo
r = n ** (1/2) # raiz quadrada 

print(f"O dobro de {n} é {d}, o triplo é {t} e a raiz quadrada é {r:.2f}")