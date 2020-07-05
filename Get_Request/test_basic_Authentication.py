import requests
from requests.auth import HTTPBasicAuth

def test_Auth():
    response=requests.get("https://api.github.com/user",auth=HTTPBasicAuth('ankit980','9807617066Aa'))
    print(response.text)