# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço normal 

#– 3x ou mais no cartão: 20% de juros

print(f"{' China Sem Galantia ':=^40}")

preco = float(input("Preço das compras: R$ "))

print('''Formas de pagamentos
[1] á vista dinheiro/cheque 10 % desconto
[2] á vista cartão de crédito/débito 5 % desconto
[3] até 2 x cartão, valor normal
[4] 3 x ou mais no cartão, acréscimo de 20 % de juros''')

op = int(input("Qual a forma de pagamento? ")) 

if op == 1:
    total = preco - (preco * 10 / 100)
    print(f"Sua compra de R$ {preco:.2f} com 10 % de desconto ficou de R$ {total:.2f}")
elif op == 2:
    total = preco - (preco * 5 / 100)
    print(f"Sua compra de R$ {preco:.2f} com 5 % de desconto ficou de R$ {total:.2f}")
elif op == 3:
    parc = preco / 2 # parcela
    print(f"A compra ficou de R$ {preco:.2f}, dividido em 2 x de R$ {parc:.2f} sem juros.")
elif op == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input("Em quantas vezes desejar parcelar? "))
    while totalparc <= 2:
        totalparc = int(input("Digite novamente: "))
    else:
        parc = total / totalparc
    print(f"A compra parcelada em {totalparc} x de R$ {parc:.2f} ficou com o valor final de R$ {total:.2f} com juros.")
else:
    print("Forma de pagamento inválida, tente novamente.")
    
    





    


