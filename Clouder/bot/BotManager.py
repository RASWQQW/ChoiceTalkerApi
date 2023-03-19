from pprint import pprint
from typing import Any, Optional
import datetime

import telethon as th
import asyncio
from GitManage.GitBash import Basher
from bot.BasicObject import BasicObject

class Manager(BasicObject):
    def __init__(self, executor: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exec = executor

    # for running await for BasicObject sessions
    def __await__(self):
        return super().__await__()

    async def Sender(self, 
                    typeIs: str, 
                    username: str, 
                    filepath: str, 
                    filename: str, 
                    path: str, 
                    chatIs: Optional[str] = "cloudeepee"):
        
        async with self.session_ as session:
            entityIs: Any = await session.get_entity(chatIs)
            # await session.send_message(entity=entityIs, message="This is my piece of genius solution")

            set_caption = (
                f"https://raswqqw.github.io/CL/files/{username}/{filename}",
                
                f"||user: {username}\n"+
                f"||filename: {filename}\n"+
                f"||type: {typeIs}\n"+
                f"||date: {datetime.datetime.now()}"
            )

            # Send file inside Cloudeepee along with set_caption's notes
            async def FileSender():
                await session.send_file(entity=entityIs, file=filepath, caption=f"{set_caption[0]}\n{set_caption[1]}")

            # totally to add and push files in hubCL
            async def BashManager():
                # to give a order to push ready files from current
                return await Basher(username=username, filepath=path).gitexec() 
                
            tasks = [BashManager(), FileSender()]
            
            # to manage with git files
            def LocRemover(future):
                print("Results", future.result(), future.result()[0][0])
                try: resultOFRun: Basher = future.result()[0][0].FileManager()
                except Exception as e: print(e.__repr__()) 
                finally: print(resultOFRun)

            tasks = asyncio.gather(*tasks); await tasks
            tasks.add_done_callback(LocRemover)
            return set_caption
        

    async def ListOfFiles(self, 
                        chatIs: Optional[str] = "cloudeepee", 
                        editMessage: tuple[bool, str]=None, 
                        ilcaption: str=None, 
                        username: str=None,
                        filename: str=None,
                        filepath: str=None):
        # getType = ilcaption.split("||")[:-1][:5]

        client: th.TelegramClient
        async with self.session_ as client:
            entityIs: Any = await client.get_entity(chatIs)

            messages = await client.get_messages(entityIs, limit=None)
            for el in messages:
                # print(type(el))
                # print(el)s
                if el.media:
                    print(el.message)
                    if editMessage[0]:
                        if all([el.message.__contains__(text) for text in [username, filename]]):
                            if editMessage[1] == "delete":
                                client.edit_message(entity=chatIs, message=el.id, text=el.message + f"\nstatus:{editMessage[1]}")
                            elif editMessage[1] == "update":
                                client.edit_message(entity=chatIs, message=el.id, text=el.message + f"\nstatus:{editMessage[1]}", file=filepath)
                        print(f"https://t.me/cloudeepee/{el.id}")

                # await el.download_media('ins')
            
async def main():
    # asyncio.run(Manager(executor="bot").Sender(chatIs="cloudeepee", username="Hal", typeIs="txt"))
    awaiter = await Manager(executor="user")
    return await awaiter.ListOfFiles(chatIs="cloudeepee", ilcaption=("user:Hal||date:2023-03-02 19:54:07.209906||type:txt"))

if __name__ == "__main__":
    asyncio.run(main())