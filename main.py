from REST import MyController
import requests
import json

url = 'https://8080-paolocaruga-09pythonche-6soazkwyaca.ws-eu90.gitpod.io/dischi'
print("url: " + url)
response = requests.get(url)
print("status code: " + str(response.status_code))

"""
url = 'https://8080-paolocaruga-09pythonche-6soazkwyaca.ws-eu90.gitpod.io/dischi'
print("url: " + url)
disco = {
            "title": "Duke",
            "artist": "Genesis",
            "year": 1980,
            "company": "A&M"      
        }

x = requests.post(url, disco)

print("Risultato")
print(x.text)
"""

