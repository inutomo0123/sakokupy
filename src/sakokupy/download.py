from ftplib import FTP
from urllib.parse import urlparse

uris = [
    'ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest',
    'ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest',
    'ftp://ftp.apnic.net/pub/stats/apnic/delegated-apnic-extended-latest',
    'ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest',
    'ftp://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-extended-latest'
]


def split_uri(uri):

    parsed_uri = urlparse(uri)

    return [parsed_uri.scheme,
            parsed_uri.netloc,
            parsed_uri.path]


def download(uri):

    splited_uri = split_uri(uri)

    with FTP(splited_uri[1]) as ftp:
        ftp.login()

        with open(splited_uri[1], 'wb') as fp:
            ftp.retrbinary(f"RETR {splited_uri[2]}", fp.write)

            ftp.quit()


def download_all(urls):

    list(map(lambda x: download(x), urls))
