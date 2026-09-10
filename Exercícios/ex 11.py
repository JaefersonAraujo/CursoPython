# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input("Qual a largura da parede? ")) # largura
al = float(input("Altura da parede? ")) # altura

ar = l * al # área
qtd = ar / 2 # quantidade de tinta

print(f"A parede tem a largura de {l:.2f} mt com uma altura de {al:.2f} mt, dando uma área total de {ar:.2f} mt².")
print(f"Uma parede de {ar:.2f} mt² será necessários {qtd:.2f} de tinta.")
