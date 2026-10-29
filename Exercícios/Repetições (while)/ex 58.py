# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

cont = 0
pc = randint(0,10)
jogador = -1

print(('-=')*5, 'Jogo de adivinhar',('-=')*5)
while pc != jogador:
    jogador = int(input("Qual o seu palpite: "))
    cont += 1
    if pc != jogador:
        print("Errou, tente outro número")
print(f"Acertou, total de {cont} tentativas.")

