"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão
na tupla.
"""
import random

numbers = tuple(random.randint(1, 10) for _ in range(5))

print(f"Números gerados: {', '.join(str(i) for i in numbers)}")
print(f"O menor número: {min(numbers)}")
print(f"O maior número: {max(numbers)}")
