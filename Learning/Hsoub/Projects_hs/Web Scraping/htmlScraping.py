import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Main_Page')
noStratchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

element = noStratchSoup.select("#mp-tfa > p")
print(element[0].getText())

