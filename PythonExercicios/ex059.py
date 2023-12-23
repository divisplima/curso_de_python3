"""
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um número: "))

continue_ = True

while continue_:
    print("-" * 40)
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa")
    option = int(input("Selecione uma opção: "))

    print("-" * 40)

    if option == 1:
        print(f"A soma de {num_1} e {num_2} é {num_1 + num_2}.")
    
    elif option == 2:
        print(f"O produto de {num_1} * {num_2} é {num_1 * num_2}.")

    elif option == 3:
        if num_1 > num_2:
            print(f"{num_1} é o maior.")
        else:
            print(f"{num_2} é o maior.")
    
    elif option == 4:
        num_1 = int(input("Digite um número: "))
        num_2 = int(input("Digite um número: "))
    
    elif option == 5:
        continue_ = False
    
    else:
        print("Digite uma opção válida.")
