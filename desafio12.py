#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com, 5% o desconto
 
import os
os.system

valor_do_produto = float(input("informe o valor do produto desejado: "))
desconto = valor_do_produto - (valor_do_produto * 5/100)

print(f"o produto que vs deseja vale R${valor_do_produto} e com o desconto ele custará {desconto:.2f}: ")
