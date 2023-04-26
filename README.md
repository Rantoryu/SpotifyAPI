# 🎵 SpotifyAPI - Data Engineering Learning Project

## 📝 Description
Simple project that retrieve data using SpotifyAPI and automatically stores it in sqlite database.
<br>
Used reference: https://developer.spotify.com/documentation/web-api/reference/get-recently-played
<br>
Feel free to use any other to get your own data.

Live Example: (WIP)

<br>

## 🚀 Run Locally

1. Clone the project

```bash
  git clone https://github.com/Rantoryu/SpotifyAPI.git/
```

2. Install dependencies

```bash
  pip install -r requirements.txt
```

3. Create Spotify App and Generate Token

Generate token using Client ID and Client Secret from your own APP (https://developer.spotify.com/dashboard)
```bash
  python.exe .\gettoken.py
```

4. Retrieve last played tracks

Retrieve last played tracks from last 7 days (Limit 50 tracks) by running:
```bash
  python.exe .\spotify.py
```
It will create tracks.sqlite database.

5. Simple convert of database to dataframe with printing it out (Optional)
```bash
  python.exe .\convert.py
```


## 🛠️ Tech Stack

Python, Sqlite


## 👨‍🚀 Show your support

Give a ⭐️ if this project helped you!
