#Escreva um programa que converta uma temperatura digitada em °C e converta para °F

import os
os.system("cls")

c = float(input("informe a temperatura atual em °C: "))
f = ((9*c)/5) + 32
print(f"a temperatura de {c}°C corresponde a {f}°F ! ")
