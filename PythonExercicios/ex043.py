"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Acima do peso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
weight = float(input("Digite seu peso (kg): "))
height = float(input("Digite sua altura (m): "))

imc = weight / (height ** 2)

print(f"Seu IMC é: {imc:.1f}")

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Acima do peso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")
