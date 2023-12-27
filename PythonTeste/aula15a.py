num = sum = 0

while True:
    num = int(input("Digite um número: "))

    if num == 999:
        break

    sum += num

print(f"A soma de todos os valores é {sum}.")
