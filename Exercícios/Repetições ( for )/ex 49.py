# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print(f"{' Tabuada de multiplicação ':=^40}")

n = int(input("Digite um número: "))

for c in range(1 , 11):
    print(f" {n} X ",(c),'=',(n * c))
print("Fim")