''' wikipediaからcountry-codeを取得する
'''

import requests
from bs4 import BeautifulSoup

URI = 'https://ja.wikipedia.org/wiki/ISO_3166-1'


def get_country(tds):

    return [tds[4].get_text(),
            tds[1].get_text(),
            tds[0].get_text().strip(),
            tds[5].get_text()]


def get_countries(soup):

    return soup.select_one('h2>span#略号一覧')\
               .parent\
               .find_next_sibling()\
               .find_next_sibling()\
               .find_next_sibling()\
               .select('table tbody tr')


def get():

    res = requests.get(URI)

    soup = BeautifulSoup(res.text, 'html.parser')

    return get_country(get_countries(soup))
