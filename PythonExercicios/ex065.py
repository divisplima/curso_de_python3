"""
Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
continue_loop = 'S'
sum = mean = 0

while continue_loop == 'S':
    num = int(input("Digite um número: "))
    sum += num
    mean += 1

    continue_loop = ''
    while continue_loop not in 'SN':
        continue_loop = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
        if continue_loop not in 'SN':
            print("Entrada inválida. Por favor, digite S para continuar ou N para parar.")
            
print(f"Média dos números digitados: {sum / mean}")
