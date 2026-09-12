# Crie um programa que leia o nome completo de uma pessoa e mostre:

# > O nome com todas as letras maiúsculas E minúsculas.

# > Quantas letras ao todo (sem considerar espaços).

# > Quantas letras tem o primeiro nome.

nome = input("Digite um nome: ") 

print(nome.upper())
print(nome.lower())
print(f"{len(nome.replace(' ',''))} letras sem os espaços.")
print(f"O primeiro nome tem: {len(nome.split()[0])} letras.")
