import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
'''print(response.status_code)
assert response.status_code ==200
#assert is used to validate the content or we use to validated the content or header

#Display the Response

#print(response.content)
#print(response.headers)
print(response.headers.get('Date'))

# Fetch Cookies
print(response.cookies)

#Fetch Encoding
print(response.encoding)

#Elapsed Time:-Time b/w sending request and receiving the  request

print(response.elapsed)'''

json_response=json.loads(response.text)
print(json_response)

# Fetch value using JSON Path
pages= jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])

#Advance Jsonpath
#first_name=jsonpath.jsonpath(json_response,'data[2].first_name')
#print(first_name[0])

# to extract all the First Name
for i in range(0,3):
    first_name=jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
    print(first_name[0])

