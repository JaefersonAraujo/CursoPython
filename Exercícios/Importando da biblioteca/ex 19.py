# Um professor quer sortear um dos seus quatro alunos para receber uma bolsa estudantil. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

print('='*8,"Sorteio bolsa estudante",'='*8)

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

print(f"O aluno escolhido foi {random.choice([a1,a2,a3,a4])}")

