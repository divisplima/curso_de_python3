'''
Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com
a data formatada.
'''
print("=" * 6, "DESAFIO 02", "=" * 6)

day = int(input("Dia: "))
month = str(input("Mês: "))
year = int(input("Ano: "))
print(f"Você nasceu no dia {day} de {month} de {year}. Correto?")
