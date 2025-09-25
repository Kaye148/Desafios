#desenvolva um programa que leia os duas notas de um aluno e calcule e mostre a sua medía

import os
os.system("cls")

m1 = float(input("informe sua média: "))
m2 = float(input("informe sua média: "))

media = (m1 + m2) / 2

print(f"sua média final foi de {media}")