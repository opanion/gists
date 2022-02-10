from urllib import response
import requests
from requests.auth import HTTPDigestAuth
user = 'user'
passwd = 'password'

url = f'http://httpbin.org/basic-auth/{user}/{passwd}'
response = requests.get(url,auth=(user, passwd))
#print(response.status_code)
#print(response.text)

#digest
url = f'http://httpbin.org/digest-auth/auth/{user}/{passwd}'
response = requests.get(url, auth=HTTPDigestAuth(user, passwd))
print(response.status_code)