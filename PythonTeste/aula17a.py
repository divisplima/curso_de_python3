num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2) # Na posição 0 adicionar o 2
num.pop() # Elimina e retorna o último elemento da lista
num.remove(2) # Remove o primeiro 2 da lista
print(num)
