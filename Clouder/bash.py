import os
import random
import datetime
import shutil
from typing import Optional
from Cupa import Cupa

class Basher(Cupa):
    def __new__(cls, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Basher, cls).__new__(cls)
        return cls.instance

    def __init__(self, filepath: Optional[str], username: Optional[str], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filepath = filepath
        self.username = username
    

    def gitexec(self):
        commands = [
            "python -V", # To check python version
            f"cd {self.gitpath}",
            "git add .",
            f'git commit -m "{self.username}{random.randint(1, 100)}{datetime.datetime.now()}" ', # set certain commit text relatively
            "git push -u origin main",
        ]
        for command in commands:
            os.system(f"cmd /c {command}")

        self.FileManager()

    def FileManager(self):
            # shutil.rmtree(self.filepath)
            files = os.listdir(self.filepath)
            self.logManager(files)
            for file in files: os.remove(os.path(self.filepath).join(file))

    def logManager(self, files):
        border = "_" * 100        
        with open("Clouder/logs/log.txt", "a") as logsource:
           logsource.write(border+'\n'+str(datetime.datetime.now())+'\n'.join(files)+'\n'+border)


if __name__ == "__main__":
    Basher().gitexec("ss")