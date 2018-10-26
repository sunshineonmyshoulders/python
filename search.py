import webbrowser, sys
if len(sys.argv) > 1:
	search = ' '.join(sys.argv[1:])
	webbrowser.open('www.google.com.br/search?q=' + search)

