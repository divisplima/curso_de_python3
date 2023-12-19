"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
"""
vehicle_speed = float(input("Velocidade do veículo (Km/h): "))

if vehicle_speed > 80:
    fine_amount = (vehicle_speed - 80) * 7

    print("Multado por excesso de velocidade.")
    print(f"Valor da multa: R${fine_amount:.2f}.")
else:
    print("Dentro do limite de velocidade. Dirija com responsabilidade.")
