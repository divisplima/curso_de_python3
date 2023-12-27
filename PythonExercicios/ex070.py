"""
Crie um programa que leia nome e preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar. No final, mostre:

a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.00.
c) Qual é o nome do produto mais barato.
"""
print("=" * 40)
print(f"{'LOJA SUPER BARATÃO':^40}")
print("=" * 40)

total_value = product_over_1000 = 0
lowest_price = None
cheapest_product_name = ''

while True:
    product_name = str(input("Nome do produto: ")).strip()
    product_price = float(input("Preço do produto R$"))

    total_value += product_price

    if product_price > 1000:
        product_over_1000 += 1

    if lowest_price is None or product_price < lowest_price:
        lowest_price = product_price
        cheapest_product_name = product_name

    continue_input = ''

    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    
    if continue_input == 'N':
        break

print("=" * 40)
print(f"Total gasto: R${total_value:.2f}.")
print(f"Ao todo {product_over_1000} produtos tem o valor acima de R$1000.")
print(f"O produto mais barato foi {cheapest_product_name} que custa R${lowest_price:.2f}.")
