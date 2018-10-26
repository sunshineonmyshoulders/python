import requests, bs4
page = requests.get('https://s155-en.ogame.gameforge.com/game/index.php?page=overview&cp=33629956')
teste = bs4.BeautifulSoup(page.read())
metal = teste.select('#resources_metal')
print(metal)




#import bs4
#>>> exampleFile = open('example.html')
#>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
#>>> elems = exampleSoup.select('#author')