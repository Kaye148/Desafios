#crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 

import os 
os.system("cls")

real = float(input("quantidade de dinheiro na carteira ? R$: "))
dolar = real / 5.28
euro = real / 6.24
yuan = real / 0.74

print(f"com R$ {real} da para comprar U${dolar:.2f} \neuro €{euro:.2f} \nyuan ¥{yuan:.2f}")