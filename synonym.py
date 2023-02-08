import requests
import json

# Source https://api-ninjas.com/api/thesaurus

# Word to search
word = 'cold'
api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
# My api key 
response = requests.get(api_url, headers={'X-Api-Key': 'QXij4e81mMsXf5HBGiDTQg==qOwYfyVHq5BO2LKO'})
# Convert request string to JSON
responseJSON = json.loads(response.text)
if response.status_code == requests.codes.ok:
    print(responseJSON["synonyms"])
else:
    print("Error:", response.status_code, response.text)