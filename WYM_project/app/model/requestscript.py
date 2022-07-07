

import requests

def summarize(source='http://model:5000/model/predict',text="""i'm immortal"""):


    headers = {
    'accept': 'application/json',
}
    json_data = {
    'text': [text, ],
}
    response = requests.post(source, headers=headers, json=json_data)
    message = response.json()['summary_text'][0]
    print(message)
    return (message)
# summarize()
