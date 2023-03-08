import requests

username = "Rass"
headers = {"Username": username}
jsons = {'image': open("osfiles/garage/test/MarkerOf.png", "rb")}
response = requests.post(url="http://localhost:4755/sendPhoto/Rass", files=jsons, headers=headers)

print(response.text)