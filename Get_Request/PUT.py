import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users/2"

# Read input Json file
file = open("C:\\Users\\Ankit\\Desktop\\CreateUser.json",'r')
json_input = file.read()
request_json = json.loads(json_input)

#print(request_json)
# MAke PUT request with JSON body

response=requests.put(url,request_json)
#print(response.content)
assert response.status_code ==200

#Parses Response to Json Format

response_json=json.loads(response.text)
update = jsonpath.jsonpath(response_json,'updatedAt')
print(update)

