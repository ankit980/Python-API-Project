import requests
import json
import jsonpath

def test_add_new_student():
    global id
    api_url="http://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Users/Ankit/Desktop/API/addnewstudent.json", 'r')
    json_response=json.loads(f.read())
    response=requests.post(api_url,json_response)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

def test_get_data():
    api_url_get="http://www.thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response=requests.get(api_url_get)
    print(response.text)