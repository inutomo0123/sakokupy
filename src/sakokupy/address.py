import ipaddress


def get_end(_list):
    ''' startとvalueのリストを元に、endを算出し辞書を返す
    '''

    return list(map(lambda y:
                    {'start': y[0], 'end': y[0] + (y[1] - 1)},
                    list(map(lambda x:
                             [ipaddress.ip_address(x[0]), x[1]],
                             _list))))


def get_network(_dict):
    ''' startとendの辞書からネットワークアドレスを算出する
    '''

    return list(map(lambda x:
                    ipaddress.summarize_address_range(
                        x['start'],
                        x['end']).__next__(), _dict))


def organize_network(_list):
    ''' ネットワークアドレスのリストを元に
    ネットワークアドレスを整理統合する
    '''

    return list(ipaddress.collapse_addresses(_list))
