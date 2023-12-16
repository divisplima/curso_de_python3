"""
Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
"""
degrees_celsius = float(input("°C: "))

degrees_fahrenheit = (degrees_celsius * 9/5) + 32

print(f"A temperatura de {degrees_celsius:.2f}°C, corresponde a {degrees_fahrenheit:.2f}°F.")
