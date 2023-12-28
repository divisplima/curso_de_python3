"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência:

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
# Tupla com nomes de produtos e seus respectivos preços
products = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(0, len(products), 2):
    print(f'{products[i]:.<30}R$ {products[i+1]:>7.2f}')
print('-' * 40)
