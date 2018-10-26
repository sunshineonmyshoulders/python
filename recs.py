import requests, bs4

res = requests.get('https://s155-en.ogame.gameforge.com/game/index.php?page=overview')
res.text
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#rec = soup.select('#scoreContentField')
print(rec)