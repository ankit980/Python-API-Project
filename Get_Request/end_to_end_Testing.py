import requests
import json
import jsonpath

def test_Add_new_data():
    api_url="http://thetestingworldapi.com/api/studentsDetails"
    file=open("C:/Users/Ankit/Desktop/API/Requestjson.json",'r')
    request_json=json.loads(file.read())
    response=requests.post(api_url,request_json)
    print(response.text)
    id=jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url="http://thetestingworldapi.com/api/technicalskills"
    f=open("C:/Users/Ankit/Desktop/API/Api_Testing_Tech.json",'r')
    request_json=json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id']=id[0]
    response=requests.post(tech_api_url,request_json)
    print(response.text)

    add_api_url="http://thetestingworldapi.com/api/addresses"
    fil=open("C:/Users/Ankit/Desktop/API/add.json",'r')
    request_json=json.loads(fil.read())
    request_json['stId']=id[0]
    response=requests.post(add_api_url,request_json)
    print(response.text)

    final_details="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response=requests.get(final_details)
    print(response.text)

