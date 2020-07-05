import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"

# Read input Jsom file
file = open("C:\\Users\\Ankit\\Desktop\\CreateUser.json",'r')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)
# MAke POST request with JSON body

response=requests.post(url,request_json)
#print(response.content)
assert response.status_code ==201

# Fetch Header from Response
print(response.headers.get("Content-Length"))

#Parses Response to Json Format

response_json=json.loads(response.text)

#Pick ID using Jason Path
id= jsonpath.jsonpath(response_json,'id')
print(id[0])
