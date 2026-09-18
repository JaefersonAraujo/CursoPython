# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos : mirim , até 14 anos infantil, até 19 anos júnior, até 25 anos sênior e acima de 25 master.

print("\033[0;34;47m Confederação Nacional de Natação \033[0m")

ano = int(input("Informe o seu ano de nascimento: "))

idade = 2026 - ano

if idade <= 9:
    print(f"Você tem {idade} anos, sua categoria é mirim.")
elif 9 < idade <=14:
    print(f"Com {idade} anos, sua categoria é infantil.")
elif 14 < idade <= 19:
    print(f"{idade} anos , disputará a categoria júnior.")
elif 19 < idade <= 25:
    print(f"Com {idade} anos, nadará na categoria sênior.")
else:
    print(f"Você tem {idade} anos, sua categoria é a master.")

    

