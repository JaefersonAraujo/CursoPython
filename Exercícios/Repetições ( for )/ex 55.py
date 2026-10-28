# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for pessoa in range(1,6):
    p = float(input(f"Digite o peso da {pessoa}° pessoa: "))

    if pessoa == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print(f"O  maior peso foi de {maior:.2f} kg.")
print(f"O menor peso foi de {menor:.2f} kg.")





