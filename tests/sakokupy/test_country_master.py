from bs4 import BeautifulSoup

from . import test_country_master_conf as conf
from sakokupy import country_master


def test_get_country():

    exp = [['JP', 'Japan', '日本', '東アジア'],
           ['US', 'United States', 'アメリカ合衆国', '北アメリカ']]

    soup = BeautifulSoup(conf.html_country, 'html.parser')

    counties = soup.select('table tr')

    result = list(map(lambda country:
                      country_master.get_country(country.select('td')),
                      counties))

    assert result == exp


def test_get_counties():

    soup = BeautifulSoup(conf.html, 'html.parser')

    countries = country_master.get_countries(soup)

    assert len(countries) == 259


def test_get():

    country_master.get()

    assert True
