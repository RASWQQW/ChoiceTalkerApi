from pprint import pprint
from typing import Any
import datetime

import telethon as th
import asyncio
from files.conf import api_id, api_hash, botApi

class Manager(object):
    def __init__(self):
        self.session = th.TelegramClient('sessions/session3', api_id, api_hash)
        
    async def Reg(self):
        await self.session.connect()
        if not await self.session.is_user_authorized():
            await self.session.sign_in(bot_token=botApi)

    async def Sender(self, chatIs: str, typeIs: str, username: str):
        await self.Reg()
        async with self.session as session:
            entityIs: Any = await session.get_entity(chatIs)

            # print(type(entityIs))
            # await session.send_message(entity=entityIs, message="This is my piece of genius solution")

            fileName = f"test.{typeIs}"
            set_caption = f"user:{username}||date:{datetime.datetime.now()}||type:{typeIs}"
            await session.send_file(entity=entityIs, file=f"garage/test/{fileName}", caption=set_caption)
            return set_caption
        
    async def ListOfFiles(self, chatIs: str, ilcaption: str):
        await self.Reg()
        getType = ilcaption.split("||")[:-1][:5]
        fileType = None
        match getType:
            case ["txt", "document", "html"]: fileType = "document"
            case ["mp3", ]: fileType = "audio"
            case ["mp4", "mov", "avi"]: fileType = "video"
            case ["png", "jpg", "jpeg", "gif", "tiff"]: fileType = "photo"

        async with self.session as client:
            entityIs: Any = await client.get_entity(chatIs)

            messages = await client.get_messages(entityIs, limit=None)
            for el in messages:
                # print(type(el))
                # print(el)
                if el.media.type == fileType:
                    print(el.id)
                    if el.photo:
                        print(el.photo.id)
                        pathIs = el.photo.caption
                        print(pathIs, type(pathIs))

                # await el.download_media('ins')
            
if __name__ == "__main__":
    asyncio.run(Manager().Sender(chatIs="cloudeepee", username="Hal", typeIs="mp4"))