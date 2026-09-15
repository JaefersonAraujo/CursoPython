# Crie um programa que leia o nome de uma cidade diga se ela começou ou não com o nome "Santo".

cid = input("Qual cidade você nasceu? ").strip()
print(cid[:5].upper() == 'SANTO')