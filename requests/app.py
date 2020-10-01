import requests
from pprint import pprint
import hashlib

# httpbin
# site para testar requests

# r = requests.get('http://127.0.0.1:5000/listar_cliente')
# res = r.json()
# f = open('data.txt', 'w+')
# f.write(str(res))
# print(r.status_code)
# pprint(res)


# r = requests.post('http://127.0.0.1:5000/listar_cliente', json={"id": "5eb45d8357d943546641b22a"})
# res = r.json()
# pprint(res)


h = hashlib.new('ripemd160')
h.update(b'baixa_estoque')
print(h.hexdigest())


f = open('hash.txt', 'w+')
f.write(str(h.hexdigest()))