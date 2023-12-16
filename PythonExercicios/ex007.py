"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
grade1 = float(input("Nota A: "))
grade2 = float(input("Nota B: "))

average = (grade1 + grade2) / 2

print(f"A sua média é de {average:.1f}.")
