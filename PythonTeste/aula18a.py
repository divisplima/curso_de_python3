pessoa = list()
galera = list()

pessoa.append('Gustavo')
pessoa.append(40)
galera.append(pessoa.copy())

pessoa[0] = 'Maria'
pessoa[1] = 19
galera.append(pessoa.copy())

print(galera)
