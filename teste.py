import time
dadosUsers = {"nomePlayer":[], "nomePJ":[], "classe":[], "raca":[]}
print ("+"+85*"-"+"+")
entradaNomePlayer =("| Olá viajante"+ 72*" "+"|"+"\n| Seja bem vindo a sua ficha inteligente e irei lhe ajudar a criar seu personage      |\n| Para começarmos me diga; como devo chamá-lo ? "+38*" "+"|\n| ") 
for letras in entradaNomePlayer:
	if letras == '\n':
		print ()
	else:
		print (letras, end = '', flush = True)
		time.sleep(0.05)
nomePlayer= input()
dadosUsers["nomePlayer"].append(nomePlayer)
tamanhoNome = len(nomePlayer)
print ("| A partir de agora é assim que irei lhe chamar: "+nomePlayer+((tamanhoNome-85)*" ")+"|")
print ("| "+nomePlayer+" Para começarmos com a criação do seu Personagem Jogavel preciso que escolha a raça     |")
def escolhaRaca(raca):
	raca = int(input("| As opções de raça são:\n| 1 - Anão\n| 2 - Elfo\n| 3 - Halfling\n| 4 - Humano\n| 5 - Draconato\n| 6 - Gnomo\n| 7 - Meio-Elfo\n| 8 - Meio-Orc\n| 9 - Tiefling\n| Digite 1 para selecionar sua raça ou 2 para mais informações das raças.\n| "))
	if raca == 2:
		infoRaca = int(input("| Qual raca deseja saber mais ?"))
		if infoRaca == 1:
			print ("| Informações dos Anãos")
		elif infoRaca == 2:
			print ("| Informações dos Elfos")
		elif infoRaca == 3:
			print ("| Informações dos Halflings")
		elif infoRaca == 4:
			print ("| Informações dos Humano")
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
	if raca > 2:
		print ("Valor inválido, tente novamente")
		escolhaRaca
