"""
Faça um programa que leia 5 valores numéricos e faça uma lista.

No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
"""
numbers = list()

for i in range(5):
    numbers.append(int(input(f"Digite o {i+1}º valor: ")))

max_value = max(numbers)
min_value = min(numbers)

max_positions = [i+1 for i, x in enumerate(numbers) if x == max_value]
min_positions = [i+1 for i, x in enumerate(numbers) if x == min_value]

print(f"O maior número digitado foi o {max_value} nas posições {', '.join(map(str, max_positions))}.")
print(f"O menor número digitado foi o {min_value} nas posições {', '.join(map(str, min_positions))}.")