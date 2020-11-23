import ipaddress

# startとvalueのリスト
l = [["41.0.0.0", 2097152],
     ["41.32.0.0", 1048576],
     ["41.48.0.0", 524288],
     ["41.56.0.0", 65536],
     ["41.57.0.0", 16384],
     ["217.77.224.0", 4096],
     ["217.151.192.0", 4096],
     ["217.151.208.0", 4096],
     ["217.173.176.0", 4096],
     ["217.197.80.0", 4096]]

# endを算出し、辞書を返す
l = list(map(lambda y:
             {'start': y[0], 'end': y[0] + y[1]},
             list(map(lambda x:
                      [ipaddress.ip_address(x[0]), x[1]],
                      l))))

# endを取得し、startとendからネットワークアドレスを取得
ll = list(map(lambda x:
              ipaddress.summarize_address_range(
                  x['start'],
                  x['end']).__next__(), l))

print(ll)

# ネットワークアドレスを統合
print(list(ipaddress.collapse_addresses(ll)))
