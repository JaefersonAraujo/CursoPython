# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase =(input("Digite uma frase: ")).lower () .replace (" ","")

inverso = ""  # frase[::-1] mesmo resultado, sem a necessidade do for

for letra in frase:
    inverso = letra + inverso

print(f"{inverso}")

if frase == inverso:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")