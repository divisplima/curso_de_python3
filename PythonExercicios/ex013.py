"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
# Store the percentage of the salary increase
SALARY_INCREASE_PERCENTAGE = 0.15

employee_salary = float(input("Salário atual: R$"))
new_employee_salary = employee_salary + (employee_salary * SALARY_INCREASE_PERCENTAGE)

print(f"O salário do funcionáro que era de R${employee_salary:.2f}, com o aumento de 15%, passa a ser R${new_employee_salary:.2f}.")
