import requests
import json

"""

data="Valkstraat 29 assenede"
url = "http://localhost:5000/conv/coordinateconversion"


response = requests.post(url,data=json.dumps(data))

if response.status_code == 200:
    data1 = response.json()
    print(data1)

else:
    response.raise_for_status()


data2 = data1
url2 = "http://localhost:1000/op/parcelarea"


response = requests.post(url2,data=json.dumps(data2))

if response.status_code == 200:
    data2 = response.json()
    print(data2)

else:
    response.raise_for_status()


url3 = "http://localhost:2000/op/watercatchmentprotectionzone"
data2 = data1

response = requests.post(url3,data=json.dumps(data2))

if response.status_code == 200:
    data3 = response.json()
    print(data3)

else:
    response.raise_for_status()

"""

url4 = "http://localhost:5000/op/subtractabledrainagesurfacearea"
data3 = [200,4,20000]

response = requests.post(url4,data=json.dumps(data3))

if response.status_code == 200:
    data3 = response.json()
    print(data3)

else:
    response.raise_for_status()





