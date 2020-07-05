import requests
import json
import jsonpath

def test_oAuth():
    token_url="http://www.thetestingworldapi.com/Token"
    data={'grant_type':'password','username':'admin','password':'adminpass'}
    response=requests.post(token_url,data)
    token_value=jsonpath.jsonpath(response.json(),'access_token')
    auth={'Authorization':'Bearer '+token_value[0]}
    print(response.text)
    api_oAuth_url="http://www.thetestingworldapi.com/StDetails/0"
    response=requests.get(api_oAuth_url,headers=auth)
    print(response.text)