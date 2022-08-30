from telethon.sync import TelegramClient
import datetime
import pandas as pd

api_id = 14822043
api_hash = 'c128d7d3b8cfb51d648f91dc916b9012'


chats = ['CM TEAM MAIN']


client =  TelegramClient('anon', api_id, api_hash)


async def main():
        me = await client.get_me()
        print(me.stringify())
        username = me.username
        print(username)
        print(me.phone)

        async for dialog in client.iter_dialogs():
                print(dialog.name, 'has ID', dialog.id)