# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0 , 2)
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input("Qual a sua jogada? "))

if 0 <= jogador <= 2:
    print('-=' * 11)
    print(f"Computador jogou {itens[pc]}")
    print(f"Jogador jogou {itens[jogador]}")
    print('-=' * 11)
    if pc == 0:                             # Jogou pedra
        if jogador == 0:
            print("Empate")
        elif jogador == 1:
            print("Jogador ganhou")
        elif jogador == 2:
            print("Computador ganhou")
        
    elif pc == 1:                           # jogou papel
        if jogador == 0:
            print("Computador ganhou")
        elif jogador == 1:
            print("Empate")
        elif jogador == 2:
            print("Jogador ganhou")
        
    elif pc == 2:                           # Jogou tesoura
        if jogador == 0:
            print("Jogador ganhou")
        elif jogador == 1:
            print("Computador ganhou")
        elif jogador == 2:
            print("Empate")
else:
    print("Opção inválida")        
                         

