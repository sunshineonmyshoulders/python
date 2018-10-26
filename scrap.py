import urllib
from urllib import request as rq

resp = rq.urlopen("https://pt.wikipedia.org")
data = resp.read()
html = data.decode("UTF-8")
print(html[:200])