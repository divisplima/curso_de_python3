def funcao():
    global n2 # Chamada da var global n2
    n2 = 10 # Var Global
    n1 = 4 # Var local
    print(f"n1 dentro vale: {n1}")
    print(f"n2 dentro vale: {n2}")


n1 = 2  # Var global
n2 = 8  # Var global
funcao()
print(f"n1 fora vale {n1}")
print(f"n2 fora vale {n2}")

