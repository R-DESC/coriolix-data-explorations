import requests

base_uri = 'http://coriolix.ceoas.oregonstate.edu/ptsur/api'

# For now we must set verify to false.
response = requests.get(base_uri, verify = False)

if response.status_code == requests.codes.ok:
    print("The API for the R/V Point Sur is up and running!")
else:
    print(f"{response.status_code} : {response.reason}")