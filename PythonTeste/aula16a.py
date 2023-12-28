lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(len(lanche))

for comida in lanche:
    print(comida)

for cont in range(len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} na posição {pos}")

print(sorted(lanche)) # Coloca a tupla em ordem de A-Z
