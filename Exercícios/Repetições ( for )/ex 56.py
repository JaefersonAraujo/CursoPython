# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
maior_idade = 0
nome_velho = ''
totmulheres = 0

for pessoa in range(1,5):
    print('-=' * 5, f"{pessoa} Cadastro", '-='*5)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    soma_idade += idade

    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        totmulheres += 1
if nome_velho == '':
    print("Nenhum nome foi cadastrado")
else:
    print(f"O homem mais velho é o {nome_velho} com {maior_idade} anos.")


print(f"A média de idade do grupo é de {soma_idade /4:.2f}")
print(f"Temos {totmulheres} mulheres com menos de 20 anos.")



        

