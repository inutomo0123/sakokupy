#import pandas as pd

#df = pd.read_csv("./ftp.apnic.net", delimiter="|")

type(df)


def comments():
    '''先頭が#である
    '''
    pass


def header_version():
    '''7列でかつ、先頭が数値である
    '''
    pass


def header_summary():
    pass


def record():
    pass


formats = {
    1: 'comments',
    7: 'header_version',
    6: 'header_summary',
    8: 'record'
}
