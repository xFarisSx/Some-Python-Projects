import bs4
from  pathlib import Path

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')

# elements = exampleSoup.select("#author")
elements = exampleSoup.find_all(attrs={'id':'author'})
print(elements)
print(elements[0].getText())
print(elements[0].attrs)
