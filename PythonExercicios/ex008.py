"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

desafio: converta m para km, hm, dam, m, dm, cm, mm
"""
length_in_meters = float(input("Comprimento (m): "))

length_in_kilometers = length_in_meters / 1000
length_in_hectometers = length_in_meters / 100
length_in_decameters = length_in_meters / 10
length_in_decimeters = length_in_meters * 10
length_in_centimeters = length_in_meters * 100
length_in_millimeters =length_in_meters * 1000

print(f"{length_in_kilometers} km.")
print(f"{length_in_hectometers} hm.")
print(f"{length_in_decameters} dam")
print(f"{length_in_meters} m.")
print(f"{length_in_decimeters:.0f} dm")
print(f"{length_in_centimeters:.0f} cm.")
print(f"{length_in_millimeters:.0f} mm.")
