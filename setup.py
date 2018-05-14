import requests

auth=('username','password')
headers={"Accept":"application/json"}

uri = 'https://index.affectiva.com'

print(requests.get(uri, auth=auth, headers=headers).json())