import webbrowser, sys, time

planetas = ['https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=33629956','https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=33630969', 'https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=33631179','https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=33631927','https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=33633458','https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=33635749']


for planet in planetas:
	webbrowser.open(planet, new=0, autoraise=True)
	arq = open('arq.txt', 'a') # abre o arquivo
	hora = time.ctime()
	arq.write(hora)
	time.sleep(3)

	
	