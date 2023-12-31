pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")

pessoas['peso'] = 98.5
del pessoas['peso']

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for keys, values in pessoas.items():
    print(f"{keys} = {values}.")
