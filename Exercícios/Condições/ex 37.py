# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número: "))

print(('-=-') * 5 + " Tabela de conversão " + ('-=-') * 5)
print('''[1] binário
[2] octal
[3] hexadecimal
''')

op = int(input("Escolha sua opção: "))

if op == 1:
    print(f"O número {num} convertido em binário é {bin(num)}")
elif op == 2:
    print(f"O número {num} convertido em octal é {oct(num)}")
elif op == 3:
    print(f"O número {num} convertido hexadecimal é {hex(num)}")
else:
    print("Opção inválida!")

