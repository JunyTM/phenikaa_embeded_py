import requests
import variableAndContrants as env

# Sử dụng ngrok để public server
base = "https://ee23-2402-800-61c7-e573-a1e1-b186-f3fe-af49.ngrok.io"
url = base + "/api/traffic"

def call():
    data = requests.get(url).json()['data']
    
    env.TIME_GREEN[0]  = data['time_green']
    env.TIME_YELLOW[0] = data['time_yellow']
    env.TIME_RED[0]    = data['time_red']
    env.TIME_EMER[0]   = data['time_emergency']

    env.IS_Emer[0] = data['is_emergency']
    env.IS_Night[0] = data['is_night']
    env.INFO_SHOW[0] = data['info_show']
    # print(data)
