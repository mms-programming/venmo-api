import requests
import json

r = requests.get('https://venmo.com/api/v5/public')


with open('data.json', 'w') as outfile:
    json.dump(r.json(), outfile)