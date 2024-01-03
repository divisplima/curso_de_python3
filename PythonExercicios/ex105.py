"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e retornar um dicionário
com as seguintes informações:

- A quantidade de notas.
- A maior nota.
- A menor nota.
- A média da turma.
- A situação (opcional).

Adicione também as docstrings da função.
"""
import numpy as np

def notas(*notas, situacao=False):
    """
    Calcula estatísticas das notas dos alunos usando NumPy.

    :param notas: Uma ou mais notas dos alunos.
    :type notas: float
    :param situacao: Indica se a situação do aluno deve ser incluída no resultado.
    :type situacao: bool
    :return: Um dicionário com as estatísticas das notas.
    :rtype: dict
    """
    if not notas:
        raise ValueError("É necessário fornecer pelo menos uma nota.")

    notas_array = np.array(notas)
    quantidade = len(notas)
    maior_nota = np.max(notas_array)
    menor_nota = np.min(notas_array)
    media = np.mean(notas_array)

    resultado = {
        'quantidade': quantidade,
        'maior_nota': maior_nota,
        'menor_nota': menor_nota,
        'media': media
    }

    if situacao:
        if media >= 7:
            resultado['situacao'] = 'Aprovado'
        elif media >= 5:
            resultado['situacao'] = 'Recuperação'
        else:
            resultado['situacao'] = 'Reprovado'

    return resultado

# Exemplo de uso
notas_alunos = [8.5, 7.2, 6.8, 9.0, 5.5]
resultado = notas(*notas_alunos, situacao=True)

# Exibindo o resultado
print("Estatísticas das Notas:")
for chave, valor in resultado.items():
    print(f"{chave.capitalize()}: {valor}")
