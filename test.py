import requests

url = "http://127.0.0.1:5000/detect-plate"
files = {'image': open('platmobil.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
