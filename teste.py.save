import time
dadosUsers = {"nomePlayer":[], "nomePJ":[], "classe":[], "raca":[]}
print ("+"+85*"-"+"+")
entradaNomePlayer =("| Olá viajante"+ 72*" "+"|"+"\n| Seja bem vindo a sua ficha inteligente eu irei lhe ajudar a criar seu personage     |\n| Para começarmos me diga; como devo chamá-lo ? "+38*" "+"|\n") 
for letras in entradaNomePlayer:
	if letras == '\n':
		print ()
	else:
		print (letras, end = '', flush = True)
		time.sleep(0.05)
nomePlayer = input()
dadosUsers["nomePlayer"].append(nomePlayer)
print ("|A partir de agora é assim que irei lhe chamar: "+nomePlayer+45*" "+"|")
print ("|"+nomePlayer+" Para começarmos com a criação do seu Personagem Jogavel preciso que escolha a raça     |")
raca = int(input("| As opções de raça são:\n| 1 - Anão\n| 2 - Elfo\n| 3 - Halfling\n| 4 - Humano\n| 5 - Draconato\n| 6 - Gnomo\n| 7 - Meio-Elfo\n| 8 - Meio-Orc\n| 9 - Tiefling\n| Digite 1 para selecionar sua raça ou 2 para mais informações das raças."))
if raca == 2:
	infoRaca = int(input("| Qual raca deseja saber mais ?"))
	if infoRaca == 1:
		print ("| Informações dos \033[1mAnãos\033[0m\n\033[1mCaracterísticas:\033[0m Robustos e resistentes, conhecidos por sua ligação com a terra e a metalurgia.\n\033[1mHabilidades:\033[0m +2 Constituição, resistência a venenos, visão no escuro, proficiência com armas.\n\033[1mSub-raças:\nAnão da Colina:\033[m +1 Sabedoria, mais pontos de vida.\n\033[1mAnão da Montanha:\033[0m +2 Força, proficiência com armaduras médias.\n\033[1mDefeitos:\ Lentos (movimento de 7,5m).\n\033[1mRelevância:\033[0m Ótimos para classes focadas em combate e resistência física.")
	elif infoRaca == 2:
		print ("| Informações dos Elfos")
	elif infoRaca == 3:
		print ("| Informações dos Halflings")
	elif infoRaca == 4:
		print ("| Informações dos \033[1mHumanos\033[0m\n| \033[1mCaracterísticas:\033[0m Versáteis e adaptáveis.\n| \033[1mHabilidades:\033[0m +1 em todos os atributos ou escolha uma variação que dá +1 em dois atributos, uma perícia extra e um talento.\n| \033[1mDefeitos:\033[0m Não têm habilidades raciais especiais.\n| \033[1mRelevância:\033[0m Excelente escolha para jogadores que querem maximizar suas opções de personalização.")
	elif infoRaca == 5:
		print ("| Informações Draconato")
	elif infoRaca == 6:
		print ("| Informações Gnomo")
	elif infoRaca == 7:
		print ("| Informações Meio-Elfo")
	elif infoRaca == 8:
		print ("| Informações Meio-Orc")
	else:
		print ("| Informações Tiefling")
else:
	raca = int(input("| Qual raça você escolheu ?"))
dadosUsers["raca"].append(raca)
