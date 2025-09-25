#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

import os 
os.system("cls")

medida = float(input("digite uma distancia me metros: "))

km = medida / 1000 
hm = medida / 100
dam = medida / 10
dm = medida *10
cm = medida * 100
mm = medida * 1000

print(f"a media de {medida}m corresponte a \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm")