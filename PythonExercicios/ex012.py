"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
DISCOUNT = 0.05

product_price = float(input("Valor do produto: R$"))
new_product_price = product_price - (product_price * DISCOUNT)

print(f"Novo preço do produto: R${new_product_price:.2f}")
