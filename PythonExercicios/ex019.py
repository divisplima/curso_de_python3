"""
O professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome escolhido.
"""
from random import choice

student1 = str(input("Aluno 1: ")).strip()
student2 = str(input("Aluno 2: ")).strip()
student3 = str(input("Aluno 3: ")).strip()
student4 = str(input("Aluno 4: ")).strip()

students_list = [student1, student2, student3, student4]
chosen_student = choice(students_list)

print(f"O aluno escolhido foi {chosen_student}.")
