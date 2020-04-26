import requests

url = "http://www.neeo.cc:6001/post"

payload = 'k1=v1'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))