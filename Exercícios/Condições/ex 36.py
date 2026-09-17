# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('>' * 5 + " Banco Agiota " + '<' * 5)
print("Simulação de Financiamento.")

casa = float(input("Valor do ímovel desejado: R$ "))
renda = float(input("Qual a sua renda mensal? "))
ano = int(input("Quantos anos pretende fazer o financiamento? "))

limite = (renda * 30) / 100 # limite máximo da prestação
meses = ano * 12
prestaçao = casa / meses

if prestaçao <= limite:
    print(f"Seu fianciamento foi aprovado, sua prestação ficou de R$ {prestaçao:.2f} com um prazo de pagamento em {ano} anos.")
    print(f"{meses} x {prestaçao:.2f}")
else: 
    print(f"Crédito Negado, sua prestação ficou com o valor de R$ {prestaçao:.2f} comprometendo sua renda mensal.")

print("Banco Agiota agradece pela preferência. ")


