brasil = list()
estado = dict()

for i in range(3):
    estado['uf'] = str(input("UF: ")).strip()
    estado['sigla'] = str(input("Sigla: ")).strip()
    brasil.append(estado.copy())
print(brasil)

for estado in brasil:
    for keys, values in estado.items():
        print(f"O campo {keys} tem valor {values}.")

for estado in brasil:
    for values in estado.values():
        print(values, end=' ')
    print()
