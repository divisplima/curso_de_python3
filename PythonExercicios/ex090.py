"""
Faça um programa que leia o nome e média e um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela. 
"""
print("=" * 40)
print(f"{'STUDENT STATUS':^40}")
print("=" * 40)

student = dict()

student['name'] = str(input("Nome: ")).strip().capitalize()
student['average'] = float(input(f"Média de {student['name']}: "))

if student['average'] >= 7.0:
    student['status'] = 'Aprovado'
elif 5.0 <= student['average'] < 7.0:
    student['status'] = 'Recuperação'
else:
    student['status'] = 'Reprovado'

print("=" * 40)
print(f"{'NOME':<20}{'MÉDIA':^10}{'STATUS':>10}")
print(f"{student['name']:<20}{student['average']:^10}{student['status']:>10}")
print("=" * 40)
