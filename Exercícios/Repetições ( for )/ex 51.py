# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

num = int(input("Digite o primeiro termo: "))

rz = int(input("Qual a razão? "))

for c in range(1, 11):
    print(f"{num}",end=" -> ")
    num += rz
print("Acabou")

