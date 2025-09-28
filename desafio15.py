#Escreva um programa que pergunte a quantidade de km percorreidos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,sabendo que o carro custa R$60 por dia e 0.15 por km rodado 

import os 
os.system("cls")

dias = int(input("quantos dias alugados ?: "))
km = float(input("quantos km rodados ?: "))
pago = (dias * 60) + (km * 0.15)
print(f"o total a pagar será de R${pago:.2f}: ")
