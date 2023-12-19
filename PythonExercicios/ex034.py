"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1 250.00, calcule um aumento de 10%.

Para inferiores ou iguais o aumento é de 15%.
"""
employee_salary = float(input("Salário atual: "))

if employee_salary > 1250:
    increase_percentage = 0.10
else:
    increase_percentage = 0.15

increase_amount = employee_salary * increase_percentage
new_employee_salary = employee_salary + increase_amount

print(f"O salário do funcionário que era de R${employee_salary:.2f} passa a ser R${new_employee_salary:.2f} com aumento de {increase_percentage * 100}%.")
