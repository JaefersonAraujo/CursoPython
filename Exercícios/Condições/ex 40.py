# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:



print("\033[0;31m Escola de Python\033[m")

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

soma = n1 + n2
media = soma/2

print(f"Tirando notas {n1} e {n2} ficou com uma média de {media:.2f}")

if media >= 7:
    print("Aluno aprovado.")
elif media >= 5:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")



