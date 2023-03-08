from pprint import pprint
from typing import Any
import datetime

import telethon as th
import asyncio
from osfiles.conf import api_id, api_hash, botApi
from bash import Basher

class Manager(object):
    def __init__(self, executor: str):
        self.exec = executor
        self.session: th = None
        
    async def open(self):
        if self.exec == "bot": _exec = "Bot"
        else: _exec = "User"
        self.session = th.TelegramClient(f'sessions/{_exec}', api_id, api_hash)
        await self.Reg()

    async def Reg(self):
        await self.session.connect()
        if not await self.session.is_user_authorized():
            await self.session.sign_in(bot_token=botApi)


    async def Sender(self, chatIs: str, typeIs: str, username: str, filepath: str, filename: str, path: str):
        await self.open()
        async with self.session as session:
            entityIs: Any = await session.get_entity(chatIs)
            # print(type(entityIs))
            # await session.send_message(entity=entityIs, message="This is my piece of genius solution")

            set_caption = (
                f"user:{username}||date:{datetime.datetime.now()}||type:{typeIs}",
                f"https://raswqqw.github.io/CL/files/{username}/{filename}"
            )
            # Send file inside Cloudeepee along with set_caption's notes
            async def FileSender():
                await session.send_file(entity=entityIs, file=filepath, caption=f"{set_caption[0]} : {set_caption[1]}")

            # totally to add and push files in hubCL
            async def BashManager():
                Basher(username=username, filepath=path).gitexec() # to give a order to push ready files from current
                
            tasks = [FileSender(), BashManager()]

            # run them as task in synch design 
            for task in enumerate(tasks):
                tasks[task[0]] = asyncio.create_task(task[1])

            await asyncio.gather(*tasks)
            return set_caption

        
    async def ListOfFiles(self, chatIs: str, ilcaption: str=None):
        await self.open()
        # getType = ilcaption.split("||")[:-1][:5]

        async with self.session as client:
            entityIs: Any = await client.get_entity(chatIs)

            messages = await client.get_messages(entityIs, limit=None)
            for el in messages:
                # print(type(el))
                # print(el)s
                if el.media:
                    print(el.message)
                    if el.message == ilcaption:
                        print(f"https://t.me/cloudeepee/{el.id}")

                # await el.download_media('ins')
            
if __name__ == "__main__":
    # asyncio.run(Manager(executor="bot").Sender(chatIs="cloudeepee", username="Hal", typeIs="txt"))
    asyncio.run(Manager(executor="user").ListOfFiles(chatIs="cloudeepee", ilcaption=("user:Hal||date:2023-03-02 19:54:07.209906||type:txt")))