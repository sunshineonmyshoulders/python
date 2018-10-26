name = input("Qual o seu nome?\n")

if len(name) <= 0:
	print("Digite um nome válido\n")
else:
	game = input(print("Olá", name,". Você gostaria de jogar um jogo? S or N\n" ))
	if game == 'S':
		print("vamos jogar\n")
	elif game == 'N':
		print("ok, até a próxima\n")
	else:
		print("Selecione uma opção válida\n")