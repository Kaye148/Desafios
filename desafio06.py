#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

import os
os.system("cls")

numero = (int(input("digite um número!: ")))

dobro = numero * 2
triplo = numero * 3
raiz = numero **(1/2)

print(f"o dobro desse número é {dobro} \no triplo é {triplo} \na raiz quadrada é {raiz:.2f}")