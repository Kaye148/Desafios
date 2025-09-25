#faça um algoritmo que leia um salário de um funcuionário e mostre seu novo salario ,com 15% de aumento.

import os
os.system

salário = float(input("informe seu salário R$ :"))
reajuste = salário + (salário  *15 /100)

print(f"o seu salário mais o reajuste de 15% ficou igual a R$ {reajuste}: ")