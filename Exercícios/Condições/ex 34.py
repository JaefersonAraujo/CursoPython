# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual o valor do salário? "))

a1 = (salario * 10) / 100 # calculo de porcentagem
a2 = (salario * 15) / 100

s1 = salario + a1 # soma
s2 = salario + a2

if salario > 1250:
    print(f"Seu salário terá um aumento de R$ {a1} ficando com o total de R$ {s1:.2f}")
else:
    print(f"Seu salário terá um aumento de R$ {a2} ficando com o total de R$ {s2:.2f}")
