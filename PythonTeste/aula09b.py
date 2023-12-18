frase = "Curso em Vídeo Python"           
print(frase.count('o'))                         # Conta quantas vezes aparece o 'o'
print(len(frase))                               # Mostra o tamanho da cadeia de caracteres
print(frase.strip())                            # Remove os espaços desnecesários
print(frase.replace('Python', 'Android'))       # Muda a substring Python para Android
print('Curso' in frase)                         # Verifica se há a palavra curso em frase
print(frase.find('Vídeo'))                      # Verifica em qual índice começa a palavra Vídeo

nova_frase = frase.split()                      # Divide as palavras e transforma numa lista
print(' '.join(nova_frase))                     # Junta as palavras e transforma numa cadeia de caracteres
