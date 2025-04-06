import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/tecnologia/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

for noticia in soup.select(".feed-post-body-title"):
    print(noticia.text.strip())
