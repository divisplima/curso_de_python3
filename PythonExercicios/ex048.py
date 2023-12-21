"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se econtram no intervalor de 1 até 500.
"""
sum = 0

for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        sum += i
print(f"A soma de todos os números ímpares múltiplos de três entre o intervalo de 1 a 500 é {sum}")
