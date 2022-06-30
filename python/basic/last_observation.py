import requests

base_uri = 'http://coriolix.ceoas.oregonstate.edu/ptsur/api'

# For now we must set verify to false.
uri = '/'.join((base_uri, 'last_obs'))

response = requests.get(uri, verify = False)

if response.status_code == requests.codes.ok:
    data = response.json()

    # Print variable names and identify time, latitude, and longitude values.
    print("List of variables.")
    for parameter in data:
        name = parameter['parameter_name']
        print(name)
        if name == 'Latitude':
            lat = parameter['value']
        elif name == 'Longitude':
            lon = parameter['value']
    time = parameter['datetime_corrected']
    print('')

    print(f"At {time}, the ship was located at {lat} N, {lon} E.")
else:
    print("Unable to access data.")