"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

student1 = str(input("Aluno 1: ")).strip()
student2 = str(input("Aluno 2: ")).strip()
student3 = str(input("Aluno 3: ")).strip()
student4 = str(input("Aluno 4: ")).strip()

students_list = [student1, student2, student3, student4]
shuffle(students_list)

print(f"Ordem de apresentação: {students_list}")
