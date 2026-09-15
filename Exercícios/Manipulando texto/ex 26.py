# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A" em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Escreva uam frase: ").strip().upper()
print(f"A letra a aparece {frase.count("A")} vezes.")
print(f"A primeira letra A aparece na posição {frase.find("A") + 1}")
print(f"A última letra A aparece na posição {frase.rfind("A") + 1}")