import os

class Cupa(object):
    def __init__(self):
        self.gitpath = 'C:\\Users\\Professional\\Documents\\GitHub\\hubCl'
        self.gitLink = 'https://github.com/RASWQQW/CL.git'
        self.LocalPath = 'mySite/hubCl' # manual setted file path
        self.FindingPath = os.path.abspath('mySite/hubCl') #for finding file from local Path
        self.RepoName = "RASWQQW/CL"

        # user info
        self.token = "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"
        