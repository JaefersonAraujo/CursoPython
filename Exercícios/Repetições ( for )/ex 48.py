# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500

s = 0                        # acumulador da soma

for c in range(1 , 501, 2):
    if c % 3 == 0:           # verifica se c é multiplo de 3
        s += c               # acrescenta um número a soma
print(f"A soma de todos os número multiplos de três são: {s}")
