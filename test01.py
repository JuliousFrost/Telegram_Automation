from telethon.sync import TelegramClient
import datetime
import pandas as pd


api_id = 14822043
api_hash = 'c128d7d3b8cfb51d648f91dc916b9012'


chats = ['rsaha17']


client =  TelegramClient(None, api_id, api_hash)
df = pd.DataFrame()


for chat in chats:
    with TelegramClient(None, api_id, api_hash) as client:
        for message in client.iter_messages(chat,reverse=True):
            print(message)
            data = { "group" : chat, "sender" : message.sender_id, "text" : message.text, "date" : message.date}

            print(data)

            temp_df = pd.DataFrame(data, index=[1])
            df = df.append(temp_df)

df['date'] = df['date'].dt.tz_localize(None)

df.to_excel("F:\\Frontend Projects\\Telegram Automation\\data_{}.xlsx".format(datetime.date.today()), index=False)