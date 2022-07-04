import requests

response = requests.get("http://127.0.0.1:5000/users/500")
print(response.status_code)
print(response.content.decode('utf-8'))

response = requests.post("http://127.0.0.1:5000/users/14",json='{"name": "moshe1234"}')
print(response.status_code)
print(response.content.decode('utf-8'))


response = requests.put("http://127.0.0.1:5000/users/140",json='{"name": "moshe12345"}')
print(response.status_code)
print(response.content.decode('utf-8'))

response = requests.delete("http://127.0.0.1:5000/users/500")
print(response.status_code)
print(response.content.decode('utf-8'))
