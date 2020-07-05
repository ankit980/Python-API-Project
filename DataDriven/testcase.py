import requests
import json
import jsonpath
import openpyxl
from DataDriven import Library


def test_Add_multiple_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/Ankit/Desktop/API/AddmultipleData.json")
    json_request = json.loads(file.read())

    obj = Library.Common("C:/Users/Ankit/Desktop/API/testData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range(2, row + 1):
        updated_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(api_url, updated_json_request)
        print(response)
