"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.
"""
first_term = int(input("Primeiro termo: "))
common_difference = int(input("Razão: "))
i = 1
more = 10
total = 0

while more != 0:
    total += more

    while i <= total:
        term = first_term + (i - 1) * common_difference
        i += 1
        print(term, end=' ')
    more = int(input("\nQuantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")