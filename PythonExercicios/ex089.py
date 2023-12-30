"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""
import numpy as np

print("=" * 40)
print(f"{'REGISTRO DE ALUNOS':^40}")
print("=" * 40)

school_report = list()
running = True

while running:
    name = str(input("Nome: ")).strip().title()
    grade1 = float(input("Nota 01: "))
    grade2 = float(input("Nota 02: "))
    average = np.mean([grade1, grade2])

    student = [name, [grade1, grade2], average]
    school_report.append(student)

    continue_input = None

    while continue_input not in ['S', 'N']:
        continue_input = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]

        if continue_input == 'N':
            running = False

print("=" * 40)
print(f"{'Nº':<4}{'NOME':<20}{'MÉDIA':>8}")
print("-" * 40)
for index, student in enumerate(school_report, start=1):
    print(f"{index:<4}{student[0]:<20}{student[2]:>8.1f}")
print("=" * 40)

running = True
while running:
    student_choice = int(input("Mostrar notas de qual aluno? (999 para encerrar): "))

    if student_choice == 999:
        running = False
    elif 1 <= student_choice <= len(school_report):
        print(f"\nNome: {school_report[student_choice-1][0]} \nNotas: {', '.join(map(str, school_report[student_choice-1][1]))}")
    else:
        print("Número de aluno inválido. Tente novamente.")
print(f"{'FIM DO PROGRAMA':=^40}")
