import requests

from configuration import SERVICE_URL

resp = requests.get(SERVICE_URL)

a = resp.json()
print(a)

