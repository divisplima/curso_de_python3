try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: ")) 
    r = a / b
except Exception as erro:
    print(f"Problema encontrado... {erro.__class__}")
else:
    print(r)
finally:
    print("Volte sempre")
