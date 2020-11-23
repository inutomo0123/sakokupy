from ftplib import FTP
from urllib.parse import urlparse

URIS = [
    'ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest',
    'ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest',
    'ftp://ftp.apnic.net/pub/stats/apnic/delegated-apnic-extended-latest',
    'ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest',
    'ftp://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-extended-latest'
]


def split_uri(uri):
    ''' uriをプロトコル、ホスト、パスに分割し、辞書を返す
    '''

    parsed_uri = urlparse(uri)

    return {'proto': parsed_uri.scheme,
            'host': parsed_uri.netloc,
            'path': parsed_uri.path}


def download(uri):
    ''' uriのファイルをダウンロードする
    '''

    splited_uri = split_uri(uri)

    with FTP(splited_uri['host']) as ftp:
        ftp.login()

        with open('/dev/stdout', 'wb') as fp:
            ftp.retrbinary(f"RETR {splited_uri['path']}", fp.write)

            ftp.quit()


def download_all():
    ''' すべてのファイルをダウンロードする
    '''

    list(map(lambda x: download(x), URIS))
