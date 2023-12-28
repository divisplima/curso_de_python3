"""
Crie um programa onde o usuário digite uma expressão qualquer que use parêntesis. Seu aplicativo deverá
analisar se a expressão passada está com os parêntesis abertos e fechados na ordem correta.
"""
expression = input("Digite uma expressão: ")
stack = []

valid_expression = True  # Variável booleana para rastrear a validade da expressão

for symbol in expression:
    if symbol == '(':
        stack.append('(')
    elif symbol == ')':
        if stack:
            stack.pop()
        else:
            valid_expression = False
            break  # Se encontrar um ')' sem correspondente '(', não precisa continuar verificando

if valid_expression and not stack:
    print("Expressão válida.")
else:
    print("Expressão inválida.")
