"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
de uma Sequência de Fibonacci.
"""
n = int(input("Digite um número: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
