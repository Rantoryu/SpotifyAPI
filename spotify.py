import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///tracks.sqlite"

#Please use your own User_ID and TOKEN (if You need one generate it through gettoken.py)
USER_ID = "p1jfbwf3b2167ylq5fne0kp63"
TOKEN = "BQA77eaXigb7tcIui7_M8V7e6l_yTMgGfGMdYjOoHglF0zENh1Uq1w7SmzO7V_IwG-hafqFiTG_cEcxVmx_gKv0ZTF8cD-UMm8JtaNY_yahpSOPNhEVTxodJGkqXkC03uSkaEj5lIIBQLfWms3viGTF9mcTqNsD5cvDYsk_izQik8XTeXtpwg42nxs_RFzqrN88LUZz8iu5h0pEaO6gRTtMvP5jsg-chsKCQmzN4ZJAGGnOZAnb9IRRBJqVmFDd-ZODanW1DYgG1t8lg952AcJI8njvbimRdRDrCkplKzbkc4MF9jEd1wPdrK0jAKiuJBY6PKCpDH67I2xiqpfhxAte6oK9b7l5ETMePFSXTlJmeQc8"

def check_if_valid_data(df: pd.DataFrame) -> bool:
    if df.empty:
        print("No songs downloaded. Finishing execution")
        return False 

    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violated")

    if df.isnull().values.any():
        raise Exception("Null values found")

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    return True

if __name__ == "__main__":

    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "Authorization" : "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
      
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []
 
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])
            
    song_dict = {
        "song_name" : song_names,
        "artist_name": artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }

    song_df = pd.DataFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])
    
    if check_if_valid_data(song_df):
        print("Data valid, proceed to Load stage")

    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('tracks.sqlite')
    cursor = conn.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    cursor.execute(sql_query)
    print("Opened database successfully")

    try:
        song_df.to_sql("tracks", engine, index=False, if_exists='append')
    except:
        print("Data already exists in the database")

    conn.close()
    print("Close database successfully")
