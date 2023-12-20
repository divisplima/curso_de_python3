"""
Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO.
- Média entre 5.0 e 6.9: RECUPERAÇÃO.
- Média 7.0 ou superior: APROVADO.
"""
grade1 = float(input("Nota 1: "))
grade2 = float(input("Nota 2: "))
average = (grade1 + grade2) / 2

print(f"Sua média: {average:.1f}")

if average < 5.0:
    print("REPROVADO.")
elif 5.0 <= average <= 6.9:
    print("RECUPERAÇÃO.")
else:
    print("APROVADO.")
