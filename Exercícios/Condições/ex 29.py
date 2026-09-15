# Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por cada Km acima do limite.

print("\033[31mAtenção radar eletrônico a frente velocidade máxima 80 Km\033[0m")

velocidade = int(input("Qual a velocidade atual? "))
multa = (velocidade - 80) * 7 

if velocidade <= 80:
    print("Você esta dentro do limite permitido!")
else:
    print(f"Acima do limite permitido você receberá uma multa no valor de R$ {multa}.")



