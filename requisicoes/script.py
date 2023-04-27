import requests

res = requests.get(url='http://httpbin.org/get')

if res:
    print(res.status_code)
    print(res.headers)
    #print(res.text)
else:
    print('AFE')
