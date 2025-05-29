import requests
import pandas as pd
from datetime import datetime, timedelta

api_key = '53ae3364036f36368188752f03970737'

def get_data(days, place):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data['list'])
    df['dt_txt'] = pd.to_datetime(df['dt_txt'])

    df = df[df['dt_txt'] <= datetime.now() + timedelta(days=days)]
    df_new = pd.DataFrame({
        "date": df["dt_txt"],
        "temp": df["main"].apply(lambda x: (x.get("temp")/10)*1.8+32), # Extract 'temp' from dictionary
        'sky': df['weather'].apply(lambda x: x[0]['main'])
    })
    return df_new.to_dict()

if __name__ == '__main__':
    print(get_data(2, 'seoul'))