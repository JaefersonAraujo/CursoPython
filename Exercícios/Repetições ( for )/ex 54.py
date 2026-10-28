# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year

maior = 0
menor = 0

for ano in range(1,8):
    nascimento = int(input(f"Qual o ano de nascimento da {ano}° pessoa? "))
    idade = ano_atual - nascimento

    if idade < 18:
        print(f"Sua idade é de {idade} anos, é de menor.")
        menor += 1
    else:
        print(f"Sua idade é de {idade} anos, ja é adulto.")
        maior += 1
    
print(f"Menores de idade: {menor}")
    
print(f"Maiores de idade: {maior}")




   


