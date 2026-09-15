# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input("Qual a distância da sua viagem? "))

p1 = viagem * 0.50 # Passagem até 200 km
p2 = viagem * 0.45 # Passagem maior que 200 km

if viagem <= 200:
    print(f"Sua viagem é de {viagem}km, o valor da passagem é de R$ {p1:.2f}")
else:
    print(f"Sua viagem é de {viagem}Km, o valor da passagem é de R$ {p2:.2f}")