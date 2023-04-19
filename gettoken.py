import requests

CLIENT_ID = 'ee39bc4d94c94f9092621b205f68044e'
CLIENT_SECRET = '1ea6e9e96ca9404787531f619437b57d'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
print(access_token)