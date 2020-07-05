import requests
param={'name':'testingworld','email':'testingwolrd@gmail.com','number':'+9165655656'}
response=requests.get('https://httpbin.org/get',params=param)
print(response.text)