import os
import pprint
import random
import datetime
import shutil
from typing import Optional

import requests
from Obj import Cupa as cp, CondCode as cc
import subprocess as sub
from subprocess import PIPE 

class Basher(cp.Cupa, cc.CondCode):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Basher, cls).__new__(cls)
        return cls.instance

    def __init__(self, 
                filepath: Optional[str] = None,
                username: Optional[str] = None,
                result : Optional[dict] = {'msg': None, 'error': None},
                *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.filepath = filepath
        self.username = username
        self.result = result

    async def gitexec(self):

        # ["cd C:\\Users\\Professional\\Documents\\GitHub\\hubCl", "git add .", "git commit -m 'att'", "git push -u origin main"]
        commands = (
            "python -V&"  # for checking a python version 
            f"cd {self.gitpath} &"+
            "git add .&" +
            f"git commit -m '{self.username}{random.randint(1, 100)}'&"+ # set certain commit text relatively
            f"git pull&"+
            "git push -u origin main"
        )
        commandExecuting = sub.Popen(args=commands, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        print("T", commandExecuting.wait())
        output, err = commandExecuting.communicate(); print(output, err)
        self.result['msg'] = output.decode()
        self.result["error"] = err.decode()

        """
        return [self.Basher(filepath=self.filepath, username=self.username, result=self.result)]
        Alternative
        """

        return [self.__class__(filepath=self.filepath, username=self.username, result=self.result)]
        # return {"filepath": self.filepath, "username": self.username, "result": self.result}

    def FileManager(self):
        assert self.filepath and self.username and self.result is not None, "Arguments are not fully difned"
        
        """
        [main 2b48135] 'Rass56'
        1 file changed, 0 insertions(+), 0 deletions(-)
        create mode 100644 files/Rass/MarkerOfRass03.10.2023.48.png
        branch 'main' set up to track 'origin/main'.
        """

        # checks file is fully psuhed upon github as long as we can just delete them
        print("InnerResult", self.result)
        # if self.result.__contains__(f"To {self.gitLink}") and self.result.__contains__("main -> main"):
        if not any(self.result['error'].lower().__contains__(rej) for rej in ["error", "reject"]):
            tt = [True if elem in self.result['msg'] else False for elem in ['0 changes', '0 insertations', '0 deletions']]
            if not all(tt):
                # shutil.rmtree(self.filepath)
                files = os.listdir(self.filepath)
                self.logManager(files)
                for file in files: 
                    os.remove(os.path.join(self.filepath, file))
                return f"Procces is succed {self.good}" 
        raise Warning(f"Procces is not fully finished{self.bad}") # if arguments are not properly 

    def logManager(self, files):
        border = "\n" + "_" * 100        
        with open("logs/log.txt", "a") as logsource:
           logsource.write(border+'\n'+str(datetime.datetime.now())+"\n"+'\n'.join(files)+'\n'+border)

if __name__ == "__main__":
    Basher().gitexec()
    