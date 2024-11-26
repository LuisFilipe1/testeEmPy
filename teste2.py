import time

# Dicionário para armazenar os dados dos usuários
dadosUsers = {"nomePlayer":[], "nomePJ":[], "classe":[], "raca":[]}

# Função para imprimir texto com delay, simulando digitação
def print_com_delay(texto, delay=0.05):
    for letra in texto:
        if letra == '\n':
            print()
        else:
            print(letra, end='', flush=True)
            time.sleep(delay)

# Exibe a introdução da ficha
print("+" + 85 * "-" + "+")
entradaNomePlayer = (
    "| Olá viajante" + 72 * " " + "|\n"
    "| Seja bem vindo a sua ficha inteligente e irei lhe ajudar a criar seu personagem |\n"
    "| Para começarmos me diga como devo chamá-lo:                                    |\n"
)

# Exibe a introdução letra por letra
print_com_delay(entradaNomePlayer)

# Input para o nome do jogador com a formatação já impressa
nomePlayer = input("| Nome: " + 76 * " " + "|\n")

# Armazenando o nome do jogador
dadosUsers["nomePlayer"].append(nomePlayer)

# Finalizando a interface com a borda
print("+" + 85 * "-" + "+")
