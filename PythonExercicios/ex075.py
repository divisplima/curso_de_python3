"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.
"""

input_numbers = tuple(int(input(f"Digite o {_+1}º valor: ")) for _ in range(4))

even_numbers = tuple(number for number in input_numbers if number % 2 == 0)

print(f"Você digitou os valores: {', '.join(str(i) for i in input_numbers)}")
print(f"O 9 apareceu {input_numbers.count(9)} vezes.")
if 3 in input_numbers:
    print(f"O primeiro valor 3 foi digitado na {input_numbers.index(3)+1}ª posição.")
else:
    print("O valor 3 não foi digitado.")
print(f"Os números pares são: {', '.join(str(i) for i in even_numbers)}")