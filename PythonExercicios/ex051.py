"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
"""
first_term = int(input("Primeiro termo: "))
common_difference = int(input("Razão: "))

for i in range(10):
    term = first_term + i * common_difference
    print(term, end=' ')
