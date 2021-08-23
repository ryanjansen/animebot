import json
import requests

token = json.load(open('token.json'))

access_token = token['access_token']

url = 'https://api.myanimelist.net/v2/anime?q=fruits&limit=10'

response = requests.get(url, headers={
    'Authorization': f'Bearer {access_token}'
})

response.raise_for_status()
anime = response.json()
response.close()
print(anime)
