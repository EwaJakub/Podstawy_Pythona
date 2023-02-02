import requests

r = requests.get('https://www.coderslab.pl/pl')

print(r.status_code)
# 200

print(r.headers['content-type'])
# 'text/html; charset=utf-8'

print(r.encoding)
# 'utf-8'

print(r.text)
# '<!DOCTYPE html><html lang="pl"><head><meta charSet="utf-8... '
