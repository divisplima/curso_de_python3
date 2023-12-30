galera = list()
dados = list()
totalmai = totalmen = 0

for i in range(3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados.copy())
    dados.clear()
print(galera)

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade.")
        totalmai += 1
    else:
        print(f"{pessoa[0]} é menor de idade.")
        totalmen += 1
print(f"Temos {totalmai} maior e {totalmen} menor.")
