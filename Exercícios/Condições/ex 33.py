# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

v1 = float(input("Primeiro valor: "))
v2 = float(input("Segundo valor: "))
v3 = float(input("Terceiro valor: "))

menor = v1

if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

maior = v1

if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

'''menor = min(v1,v2,v3)
maior = max(v1,v2,v3)'''

print(f"O menor valor é {menor}")
print(f"O maior valor é {maior}")



