"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
"""
distance = float(input("Digite a distância da viagem em quilômetros: "))
travel_cost = distance * 0.50 if distance <= 200 else distance * 0.45

print(f"O custo da passagem para uma viagem de {distance} Km é R${travel_cost:.2f}.")
