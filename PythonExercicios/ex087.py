"""
Aprimore o desafio anterior, mostrando no final:

a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
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

sum_even_values = 0
sum_third_column = 0
max_value_second_row = max(matrix[1])

for i in range(3):
    for j in range(3):
        if matrix[i][j] % 2 == 0:
            sum_even_values += matrix[i][j]

        if j == 2:
            sum_third_column += matrix[i][j]

print(f"\nSoma de todos os valores pares: {sum_even_values}")
print(f"Soma dos valores da terceira coluna: {sum_third_column}")
print(f"O maior valor da segunda linha: {max_value_second_row}")
