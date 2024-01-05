from módulos import util

def main():
    num = int(input("Digite um número: "))
    fat = util.fatorial(num)
    print(f"O fatorial de {num} é {fat}.")


if __name__ == "__main__":
    main()
