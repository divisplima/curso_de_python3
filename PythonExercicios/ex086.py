"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta.
"""
matrix = list()

for i in range(3):
    row = list()
    for j in range(3):
        value = int(input(f"Insira um valor para a posição [{i+1}, {j+1}]: "))
        row.append(value)
    matrix.append(row)

print("Matriz:")
for row in matrix:
    for element in row:
        print(f"{element:^5}", end="")
    print()
