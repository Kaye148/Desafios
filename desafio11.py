#faça um programa que leia a largura e a altura de uma parede em metros,calcule a sua área e a quantidade de tinta necessária para pinta-la,sabendo que cada litro de tinta,pinta uma aréa de 2m².

import os
os.system("cls")

largura = float(input("informe a largura da parede: "))
altura = float(input("informe a altura da parede: "))
area = largura*altura
tinta = area /2 

print(f"sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m² a quantidade de tinta necessaria será de {tinta}l de tinta." )


