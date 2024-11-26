const rl = required ('readline-sync')
const personagens = [
nome_player{}
nome_pj{}
classe{}
raca{}
]
let nome = rl.question('Olá caro viajante\nSeja bem-vindo ao sua ficha inteligente\nPara facilitar nossa comunicação me diga como devo chama-lo?')
while nome == (''):
print("O nome não pode ficar em branco")
if nome != (""):
print("Tudo bem a partir de agora é assim que irei lhe chamar: "nome)
