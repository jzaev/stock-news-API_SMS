import requests
from twilio.rest import Client

account_sid = "AC68959a76a5bdb1731ca82b30eddc78fb"
auth_token = "2ee59439b9abb245df8521e1d35815dc"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

A_API_KEY = "3T9KRDK4LEXJ6DMZ"
N_API_KEY = "68d4a6b43efe4b0cb270535e345819df"

PERSENT = 5

request_parameters = {
    "apikey": A_API_KEY,
    "function": "TIME_SERIES_WEEKLY",
    "symbol": STOCK_NAME,
}

respond = requests.get(url=STOCK_ENDPOINT, params=request_parameters)
data = respond.json()["Weekly Time Series"]
date_list = list(data)[:2]
data_list = [float(data[x]["4. close"]) for x in date_list]

if abs(data_list[0] - data_list[1]) > data_list[0] * PERSENT / 100:
    print("Something happens")

request_parameters = {
    "apiKey": N_API_KEY,
    "sortBy": "publishedAt",
    "q": COMPANY_NAME,
    "totalResults": 3,
    "from": "2023-01-20"
}

respond = requests.get(url=NEWS_ENDPOINT, params=request_parameters)
data = respond.json()
articles = data["articles"][:3]

for article in articles:
    print(article["url"])

to_send = [(article["title"], article["description"]) for article in articles]
client = Client(account_sid, auth_token)
message = client.messages.create(body=to_send[0][:50], from_='+18125944733', to='+972532857801')
message = client.messages.create(body=to_send[1][:50], from_='+18125944733', to='+972532857801')

print(message.status)
