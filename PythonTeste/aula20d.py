def soma(* valores):
    s = 0

    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}.")


soma(2, 5)
soma(2, 5, 7)
