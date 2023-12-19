"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
number1 = int(input("Digite um número: "))
number2 = int(input("Digite um número: "))
number3 = int(input("Digite um número: "))

if number1 > number2 and number1 > number3:
    largest_number = number1
if number2 > number1 and number2 > number3:
    largest_number = number2
if number3 > number1 and number3 > number2:
    largest_number = number3

if number1 < number2 and number1 < number3:
    smallest_number = number1
if number2 < number1 and number2 < number3:
    smallest_number = number2
if number3 < number1 and number3 < number2:
    smallest_number = number3

print(f"O maior número é o {largest_number}.")
print(f"O menor número é o {smallest_number}.")
