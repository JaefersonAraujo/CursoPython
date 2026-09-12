# Faça um programa que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

sa = float(input("Digite salário: R$ ")) # salário
au = (sa * 15) / 100 # aumento
ns = au + sa # novo salário

print(f"Parabéns você receberá um aumento de R$ {au:.2f} seu novo salário será de R$ {ns:.2f}")
