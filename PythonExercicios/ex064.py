"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).
"""
# Versão do Guanabara
number = counter = sum = 0
number = int(input("Digite um número (999 para parar): "))

while number != 999:
    sum += number
    counter += 1
    number = int(input("Digite um número (999 para parar): "))
print(f"Você digitou {counter} números e a soma entre eles foi {sum}.")
