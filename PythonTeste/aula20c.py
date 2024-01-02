def dobra(lst):
    pos = 0
    
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2, 4, 6, 8, 0]
dobra(valores)
print(valores)
