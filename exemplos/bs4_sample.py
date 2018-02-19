#exemplo basico de BeautifulSoup
import requests
import bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))

# #methods
# soup.select('div')#tudo q foi nomeado como div
# soup.select('#author')#tudo com id igual author
# soup.select('.notice')#tudo q usa a classe css notice
# soup.select('div span')#todos os span dentro de div
# soup.select('div > span')#span dentro de um div sem nd entre eles
# soup.select('input[name]')#input nomeados como name
# soup.select('input[type="button"]')#botoes
