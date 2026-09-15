# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

pc = randint(0 , 5) # Sorteia um número 
print('-=-'*20)
print("Pense em um número entre 0 e 5. Tente ganhar da IA")
print('-=-'*20)
jogador = int(input("Escolha um número: "))
print("Processando...")
sleep(2) # pausa o programa por determinado tempo

if jogador == pc:
    print("Voçê ganhou!!")
else:
    print(f"Voçê perdeu amigo pensei no número {pc}:)")






