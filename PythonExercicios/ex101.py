"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de 
uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas
eleições.
"""
from datetime import date

def voto(birth_year, current_year):
    """
    Determina se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO com base no ano de nascimento.

    Parâmetros:
    - birth_year (int): O ano de nascimento da pessoa.
    - current_year (int): O ano atual.

    Retorna:
    str: Uma mensagem indicando o status do voto.
    """
    age = current_year - birth_year
    
    if age < 16:
        return f"Com {age} anos: VOTO NEGADO"
    elif 16 <= age < 18 or age >= 65:
        return f"Com {age} anos: VOTO OPCIONAL"
    else:
        return f"Com {age} anos: VOTO OBRIGATÓRIO"


def main():
    birth_year = int(input("Qual seu ano de nascimento? "))
    current_year = date.today().year
    print(voto(birth_year, current_year))    


if __name__ == "__main__":
    main()
