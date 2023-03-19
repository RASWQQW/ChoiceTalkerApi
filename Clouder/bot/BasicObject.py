import os
import telethon as th
from osfiles.conf import api_id, api_hash, botApi


class BasicObject(object):
    def __init__(self):
        self.session_: th = None # for proceeding a sesion for instances


        # running required functions
        ...
        
    def __await__(self):
        return self._open().__await__()   
    
    # for opening certain session
    async def _open(self):
        async def __open():
            if self.exec == "bot": _exec = "Bot"
            else: _exec = "User"

            getsessionspath = __file__.replace(os.path.basename(__file__), "sessions/")
            # open session through the giving certain arguments
            self.session_ =  th.TelegramClient(f'{getsessionspath}{_exec}', api_id, api_hash)
            print("Session: ", self.session_)
            await self.Reg() # for giving a
        await __open()

    # for registration 
    async def Reg(self):
        print("Session:", self.session_)
        await self.session_.connect()
        if not await self.session_.is_user_authorized():
            await self.session_.sign_in(bot_token=botApi)