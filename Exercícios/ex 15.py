# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por km rodado.

dias = int(input("Escolha quantos dias pretende alugar o veículo: "))
km = float(input("Determine a quilometragem a ser percorrido: "))

diária = dias * 60
rodado = km * 0.15

print(f"{dias} dias será R$ {diária:.2f}")
print(f"{km:.2f} km rodados custará {rodado:.2f}")
print(f"Valor total do aluguel é de R$ {diária + rodado:.2f}")

