import requests

#Please use your own CLIENT_ID and CLIENT_SECRET to generate token. You can create your own APP here: https://developer.spotify.com/dashboard
CLIENT_ID = ''
CLIENT_SECRET = ''

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']
print(access_token)