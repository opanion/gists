import requests

response = requests.get('http://httpbin.org/json')
#print(response.status_code)
#response.raise_for_status()
#print(response.json())
#print(response.headers['content-type'])

response = requests.get('http://httpbin.org/xml')
#print(response.status_code)
#response.raise_for_status()
#print(response.json())
print(response.headers['content-type'])
