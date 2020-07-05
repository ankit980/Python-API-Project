import requests
import json
import jsonpath

def test_add_student_data():
    api_url="http://thetestingworldapi.com/api/studentsDetails"
    f=open("C:/Users/Ankit/Desktop/API/Requestjson.json",'r')
    json_request=json.loads(f.read())
    response=requests.post(api_url,json_request)
    print(response.text)


def test_update_student_data():
    api_url="http://thetestingworldapi.com/api/studentsDetails/52458"
    f=open("C:/Users/Ankit/Desktop/API/Requestjson.json",'r')
    json_request=json.loads(f.read())
    response=requests.put(api_url,json_request)
    print(response.text)

def test_delete_student_data():
    api_url="http://thetestingworldapi.com/api/studentsDetails/52458"
    response=requests.delete(api_url)
    print(response.text)


def test_get_student_data():
    api_url="http://thetestingworldapi.com/api/studentsDetails/52458"
    response=requests.get(api_url)
    json_response=json.loads(response.text)
    print(json_response)
    id=jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0] == 52458