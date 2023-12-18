"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex.: 1834

Unidade: 4
Dezena: 3
Centena: 8
Unidade de Milhar: 1
"""
number = int(input("Insira um número qualquer: "))

unit = number % 10
ten = (number // 10) % 10
hundred = (number // 100) % 10
thousand = (number // 1000) % 10

print(f"Unidade: {unit}\nDezena: {ten}\nCentena: {hundred}\nU. Milhar: {thousand}")
