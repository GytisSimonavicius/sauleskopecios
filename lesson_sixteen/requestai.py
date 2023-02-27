import requests

rsp = requests.get('https://www.google.com')
print(rsp.status_code)
