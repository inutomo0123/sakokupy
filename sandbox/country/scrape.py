import requests
from bs4 import BeautifulSoup

uri = 'https://ja.wikipedia.org/' \
    + 'wiki/%E5%9B%BD%E5%90%8D%E3%82%B3%E3%83%BC%E3%83%89'

uri = 'https://ja.wikipedia.org/wiki/ISO_3166-1'

res = requests.get(uri)

soup = BeautifulSoup(res.text, 'html.parser')

print(soup.find('title').get_text())

print(soup.select_one('title').get_text())

print(soup.title.get_text())

print(soup.title)

from pprint import pprint as pp

#pp(soup.select('h2>span#略号一覧'))
#pp(soup.select('h2:has( h2>span#略号一覧 )'))

print(soup.select_one('h2>span#略号一覧').parent)
print(soup.select_one('h2>span#略号一覧').parent.find_next_siblings())
#print(soup.select_one('h2>span#略号一覧').parent.parent.select('table tbody tr'))
print(soup.select_one('h2>span#略号一覧').parent.find_next_siblings()[0]\
      .select_one("table"))
