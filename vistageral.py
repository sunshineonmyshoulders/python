

import webbrowser, sys

solitude = '33629956'
nmap = '33630969'
wireshark = '33631179'
metasploit = '33631927'
burpsuite = '33633458'
ettercap = '33635749'

if len(sys.argv) > 1:
	planet = ' '.join(sys.argv[1:])
	if planet == "solitude":
		webbrowser.open('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=' + solitude)
	elif planet == "nmap":
		webbrowser.open('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=' + nmap)
	elif planet == "wireshark":
		webbrowser.open('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=' + wireshark)
	elif planet == "metasploit":
		webbrowser.open('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=' + metasploit)
	elif planet == "burpsuite":
		webbrowser.open('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=' + burpsuite)
	elif planet == "ettercap":
		webbrowser.open('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=' + ettercap)
	else:
		print("Digite um planeta válido.")


	#search = ' '.join(sys.argv[1:])

#webbrowser.open('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=' + nmap)

