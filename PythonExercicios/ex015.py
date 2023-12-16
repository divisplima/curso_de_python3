"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60.00 por dia e
R$0.15 por km rodado.
"""
DAILY_RENTAL_RATE = 60
PER_KM_RATE = 0.15

distance_travelled = float(input("Quantos Km percorridos? "))
days_rented = int(input("Dias alugados: "))

total_price = (DAILY_RENTAL_RATE * days_rented) + (distance_travelled * PER_KM_RATE)

print(f"Preço a pagar: R${total_price:.2f}")
