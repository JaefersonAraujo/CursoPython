# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input("Qual o seu ano de nascimento? "))

idade = 2026 - ano


if idade < 18:
    prazo = 18 - idade
    print(f"Sua idade é de {idade} anos, faltam {prazo} anos para o seu alistamento.")
elif idade == 18:
    print(f"Você tem {idade} anos, Chegou a hora recruta do seu alistamento.  ")
else:
    prazo = idade - 18
    print(f"Já passaram {prazo} anos que seu alistamento esta pendente, idade atual é de {idade} vá até o quartel mais próximo e regularize sua situação.")

