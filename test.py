# This is just to provide an example of how the library can be used.
# Make sure you set password and username.
from sesarwslib import sesarwsclient as ws

username = ''  # Set but don't check-in.
password = ''  # Set but don't check-in.
user_code = ''  # Set but don't check-in.

sample = ws.Sample(
    user_code,
    'Individual Sample',
    'Rock',
    user_code + '1234',
    'TestSample123',
    'Igneous>Plutonic>Felsic',
    'arkose',
    '6.5',
    '13',
    'Grab',
    '35.5134',
    '-117.3463',
    '781.4',
    'Lava Mountains, Mojave Desert, California',
    'United States',
    'California',
    'San Bernardino',
    'J. E. Andrew',
    'January 01, 2010',
    'University of Kansas')

client = ws.IgsnClient(username, password)

print client.get_user_codes()
client.register_sample(sample)
print ws.IgsnClient.list_igsns(username, 10, 1)
