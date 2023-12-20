name = str(input("Digite o seu nome: ")).strip()

if name == 'Gustavo':
    print("Que nome bonito você tem!")
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
    print("Seu nome é tão popularo no Brasil!")
else:
    print("Seu nome é bem normal.")

print(f"Tenha um bom dia, {name}!")
