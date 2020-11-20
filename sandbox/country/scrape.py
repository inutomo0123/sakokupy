import requests
from bs4 import BeautifulSoup

uri = 'https://ja.wikipedia.org/wiki/ISO_3166-1'

res = requests.get(uri)

soup = BeautifulSoup(res.text, 'html.parser')

#print(soup.find('title').get_text())
#
#print(soup.select_one('title').get_text())
#
#print(soup.title.get_text())
#
#print(soup.title)

from pprint import pprint as pp

#pp(soup.select('h2>span#略号一覧'))
#pp(soup.select('h2:has( h2>span#略号一覧 )'))

#print(soup.select_one('h2>span#略号一覧').parent)

#print(soup.select_one('h2>span#略号一覧').parent.find_next_siblings())
#print(soup.select_one('h2>span#略号一覧').parent.parent.select('table tbody tr'))

#print(soup.select_one('h2>span#略号一覧').parent.find_next_siblings()[0]\
#      .select("table tbody tr ")
#      )

tr = soup.select_one('h2>span#略号一覧').parent.find_next_sibling().find_next_sibling().find_next_sibling().select('table tbody tr')

def row(td):

    return [td[4].get_text(),
            td[1].get_text(),
            td[0].get_text().strip(),
            td[5].get_text()]








pp(list(map(lambda x:
         row(x.select('td')),
         list(filter(lambda tr_ch: len(tr_ch.select('td')) == 7, tr))
         )))

#print(list(filter(lambda tr_ch: len(tr_ch.select('td')) == 7, tr)))
