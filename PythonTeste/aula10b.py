n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
m = (n1 + n2) / 2
print(f"Sua média é {m:.1f}")
print("PARABÉNS" if m >= 6.0 else "ESTUDE MAIS!")
