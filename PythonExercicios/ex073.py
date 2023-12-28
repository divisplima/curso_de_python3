"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Apenas os 5 primeiros colocados.
b) Os 4 últimos colocados na tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição da tabela está o time da Chapecoense.
"""
brazilian_teams = (
    "Palmeiras - SP",
    "Grêmio - RS",
    "Atlético Mineiro Saf - MG",
    "Flamengo - RJ",
    "Botafogo - RJ",
    "Red Bull Bragantino - SP",
    "Fluminense - RJ",
    "Athletico Paranaense - PR",
    "Internacional - RS",
    "Fortaleza - CE",
    "São Paulo - SP",
    "Cuiabá Saf - MT",
    "Corinthians - SP",
    "Cruzeiro - MG",
    "Vasco da Gama - RJ",
    "Bahia - BA",
    "Santos - SP",
    "Goiás - GO",
    "Coritiba - PR",
    "América-MG - MG"
)

print(f"Os cinco primeiros colocados: {', '.join(brazilian_teams[:5])}.")
print(f"Os quatro últimos colocados: {', '.join(brazilian_teams[-4:])}.")
print(f"Em ordem de A-Z: {', '.join(sorted(brazilian_teams))}")
try:
    chapecoense_position = brazilian_teams.index("Chapecoense - SC") + 1
    print(f"O time da Chapecoense está na {chapecoense_position}ª posição.")
except ValueError:
    print("O time da Chapecoense não faz parte dos 20 primeiros colocados.")
