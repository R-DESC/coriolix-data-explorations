import requests
import pandas as pd
import matplotlib.pyplot as plt

base_uri = 'http://coriolix.ceoas.oregonstate.edu/ptsur/api'
uri = '/'.join((base_uri, 'tsg_flth'))
params = {'date_after':'2022-06-29 04:00:00',
          'format':'json'}

# Issue the request and get data.
response = requests.get(uri, verify = False,params = params)
data = response.json()

#Place into a pandas DataFrame for easier manipulation.
df = pd.DataFrame(data)
df.index = pd.to_datetime(df.datetime_corrected) #Index the data by time.

# Show some info about the data
df.head()
df.describe().transpose()

#Plot the data
fig, ax = plt.subplots(2,1,sharex = True, constrained_layout = True)
ax[0].scatter(df.index, df.temperature, c='red')
ax[1].scatter(df.index, df.salinity, c = 'blue')

ax[0].set_ylabel('Temperature (degC)')
ax[1].set_ylabel("Salinity (PSU)")
ax[1].set_xlabel('Datetime (UTC)')
fig.suptitle("Salinity and Temperature vs Time")

plt.show()