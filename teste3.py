import time
from colorama import init, Fore, Style

# Inicializa o colorama para o Windows
init(autoreset=True)

# Função para exibir texto com efeito de digitação lenta
def typing_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Dicionário para armazenar dados do usuário
dadosUsers = {"nomePlayer": [], "raca": []}

# Introdução
typing_effect(Fore.CYAN + "| Olá viajante! Seja bem-vindo à sua ficha inteligente.")
typing_effect("| Eu irei lhe ajudar a criar seu personagem. Para começarmos, me diga o seu nome.")

# Captura o nome do jogador
nomePlayer = input(Fore.GREEN + "| Nome: ")
dadosUsers["nomePlayer"].append(nomePlayer)
typing_effect(Fore.YELLOW + f"| A partir de agora, é assim que irei lhe chamar: {nomePlayer}")
typing_effect(f"| {nomePlayer}, para começarmos com a criação do seu Personagem Jogável, escolha uma raça.")

# Lista de raças
racas = [
    "Anão", "Elfo", "Halfling", "Humano", "Draconato", "Gnomo", "Meio-Elfo", "Meio-Orc", "Tiefling"
]

# Função para exibir as raças disponíveis
def listar_racas():
    typing_effect(Fore.MAGENTA + "| As opções de raça são:")
    for i, raca in enumerate(racas, 1):
        print(Fore.CYAN + f"| {i} - {raca}")

# Função para exibir informações sobre cada raça
def mostrar_info_raca(opcao):
    info = {
        1: "| Informações dos Anões: Robustos e resistentes, conhecidos por sua ligação com a terra e a metalurgia.",
        2: "| Informações dos Elfos: Elegantes e ágeis, com afinidade para magia e a natureza.",
        3: "| Informações dos Halflings: Pequenos e corajosos, valorizam a família e a comunidade.",
        4: "| Informações dos Humanos: Versáteis e adaptáveis, +1 em todos os atributos.",
        5: "| Informações dos Draconatos: Descendentes de dragões, têm habilidades de sopro elemental.",
        6: "| Informações dos Gnomos: Inventivos e curiosos, são excelentes artesãos e estudiosos.",
        7: "| Informações dos Meio-Elfos: Carregam o melhor de elfos e humanos, bons em diplomacia.",
        8: "| Informações dos Meio-Orcs: Fortes e implacáveis, valorizam a força e a honra.",
        9: "| Informações dos Tieflings: Descendentes de demônios, têm resistência a fogo e habilidades sombrias."
    }
    typing_effect(Fore.LIGHTBLUE_EX + info.get(opcao, "| Informações não disponíveis."))

# Exibe raças e permite ao usuário escolher
while True:
    listar_racas()
    try:
        raca = int(input(Fore.GREEN + "| Escolha a raça (1-9): "))
        if 1 <= raca <= 9:
            dadosUsers["raca"].append(racas[raca - 1])
            typing_effect(Fore.YELLOW + f"| Você escolheu a raça: {racas[raca - 1]}")
            mostrar_info_raca(raca)
            break
        else:
            print(Fore.RED + "| Opção inválida. Por favor, escolha um número entre 1 e 9.")
    except ValueError:
        print(Fore.RED + "| Entrada inválida. Por favor, insira um número.")

typing_effect(Fore.CYAN + "| Obrigado por criar seu personagem! Agora você está pronto para a aventura.")

# Exibir dados finais do jogador
print(Fore.GREEN + f"| Nome do Jogador: {dadosUsers['nomePlayer'][0]}")
print(Fore.GREEN + f"| Raça Escolhida: {dadosUsers['raca'][0]}")
import time
from colorama import init, Fore, Style

# Inicializa o colorama para o Windows
init(autoreset=True)

# Largura fixa para a "folha"
LARGURA_FOLHA = 80

# Função para exibir texto com efeito de digitação lenta e bordas alinhadas
def typing_effect(text, delay=0.05):
    # Preenche com espaços até atingir a largura da folha, deixando espaço para a borda
    linha_formatada = f"| {text}".ljust(LARGURA_FOLHA - 1) + "|"
    for char in linha_formatada:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Dicionário para armazenar dados do usuário
dadosUsers = {"nomePlayer": [], "raca": []}

# Introdução
typing_effect(Fore.CYAN + "Olá viajante! Seja bem-vindo à sua ficha inteligente.")
typing_effect("Eu irei lhe ajudar a criar seu personagem. Para começarmos, me diga o seu nome.")

# Captura o nome do jogador
nomePlayer = input(Fore.GREEN + "| Nome: ")
dadosUsers["nomePlayer"].append(nomePlayer)
typing_effect(Fore.YELLOW + f"A partir de agora, é assim que irei lhe chamar: {nomePlayer}")
typing_effect(f"{nomePlayer}, para começarmos com a criação do seu Personagem Jogável, escolha uma raça.")

# Lista de raças
racas = [
    "Anão", "Elfo", "Halfling", "Humano", "Draconato", "Gnomo", "Meio-Elfo", "Meio-Orc", "Tiefling"
]

# Função para exibir as raças disponíveis
def listar_racas():
    typing_effect(Fore.MAGENTA + "As opções de raça são:")
    for i, raca in enumerate(racas, 1):
        typing_effect(f"{i} - {raca}")

# Função para exibir informações sobre cada raça
def mostrar_info_raca(opcao):
    info = {
        1: "Informações dos Anões: Robustos e resistentes, conhecidos por sua ligação com a terra e a metalurgia.",
        2: "Informações dos Elfos: Elegantes e ágeis, com afinidade para magia e a natureza.",
        3: "Informações dos Halflings: Pequenos e corajosos, valorizam a família e a comunidade.",
        4: "Informações dos Humanos: Versáteis e adaptáveis, +1 em todos os atributos.",
        5: "Informações dos Draconatos: Descendentes de dragões, têm habilidades de sopro elemental.",
        6: "Informações dos Gnomos: Inventivos e curiosos, são excelentes artesãos e estudiosos.",
        7: "Informações dos Meio-Elfos: Carregam o melhor de elfos e humanos, bons em diplomacia.",
        8: "Informações dos Meio-Orcs: Fortes e implacáveis, valorizam a força e a honra.",
        9: "Informações dos Tieflings: Descendentes de demônios, têm resistência a fogo e habilidades sombrias."
    }
    typing_effect(Fore.LIGHTBLUE_EX + info.get(opcao, "Informações não disponíveis."))

# Exibe raças e permite ao usuário escolher
while True:
    listar_racas()
    try:
        raca = int(input(Fore.GREEN + "| Escolha a raça (1-9): "))
        if 1 <= raca <= 9:
            dadosUsers["raca"].append(racas[raca - 1])
            typing_effect(Fore.YELLOW + f"Você escolheu a raça: {racas[raca - 1]}")
            mostrar_info_raca(raca)
            break
        else:
            typing_effect(Fore.RED + "Opção inválida. Por favor, escolha um número entre 1 e 9.")
    except ValueError:
        typing_effect(Fore.RED + "Entrada inválida. Por favor, insira um número.")

typing_effect(Fore.CYAN + "Obrigado por criar seu personagem! Agora você está pronto para a aventura.")

# Exibir dados finais do jogador
typing_effect(Fore.GREEN + f"Nome do Jogador: {dadosUsers['nomePlayer'][0]}")
typing_effect(Fore.GREEN + f"Raça Escolhida: {dadosUsers['raca'][0]}")
