"""
Escreva um programa para aprovar o empréstimo bancário para aprovar a compra de uma casa. O programa
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado.
"""
house_value = float(input("Valor da casa: R$"))
buyer_salary = float(input("Salário do comprador: R$"))
payment_duration_years = int(input("Anos de financiamento: "))

monthly_payment = house_value / (payment_duration_years * 12)

if monthly_payment <= (0.3 * buyer_salary):
    print("Empréstimo aprovado!")
    print(f"Prestação mensal: R${monthly_payment:.2f}")
else:
    print("Empréstimo negado. A prestação mensal excede 30% do salário.")
