# DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: (equilátero, isósceles e escaleno.)




l1 = float(input("Primeiro valor: "))
l2 = float(input("Segundo valor: "))
l3 = float(input("Terceiro valor: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("pode formar um triângulo", end=' ')
    if l1 == l2 == l3:
        print("equilátero.")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("escaleno.")
    else: 
     print("isósceles.")
else:
    print("Não pode formar um triângulo.")

