
import requests
def test_api_1():

   response : response = requests.get("https://reqres.in/api/users?page=2")
   assert response.status_code == 200
   json_data = response.json()
   print(json_data)

