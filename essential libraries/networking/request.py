import requests

response = requests.get('http://httpbin.org/xml')
#print(response.status_code)
#print(response.text)

args = dict(key1=1, key2=2, key3=False)

#response = requests.get('http://httpbin.org/get', params=args)
#print(response.url)
#print(response.text)

response = requests.post('http://httpbin.org/post', data=args)
#print(response.url)
#print(response.text)

#use a custom header
header = dict(this_is_my_header='my custom header')
response = requests.get('http://httpbin.org/get', headers=header)
#print(response.status_code)
print(response.text)