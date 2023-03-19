from github import Github 
from ...Clouder.Obj import Cupa
from testFor import Manager

class GitApi(Cupa):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GitApi, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = Github(self.token)

    def addFile(self):
        with open("osfiles/garage/test/MarkerOf.png", "rb") as f:
            file = f.read()

        tt = self.object.get_repo(self.RepoName)
        tt.create_file("files/test.png", "wonder", file, branch="main")


    def deleteFile(self, username: str, filename: str):
       repository = self.object.get_repo(self.RepoName)
       contentIs = repository.get_contents(f"files/{username}/{filename}", ref="forDelete")
       deletingResult = repository.delete_file(contentIs.path, f"{username} deleting", contentIs.sha, branch="main")
       print(deletingResult)


       Manager.ListOfFiles()
    
    def update(self, username: str, filename: str, filepath: str):
        repo = self.object.get_repo(self.RepoName)
        # content = repo.get_contents(f"files/{username}/{filename}", ref="forUpdate")
        content = repo.get_contents(f"files/test.text")
        
        print(content.name)


        # with open(filepath, "rb") as filePath:
        #     content = filePath.read()

        # repo.update_file(path=content.path,content=content, sha=content.sha, branch="main")

        ...
    
    def Performing(self):
        # perform = self.object.get_repo("RASWQQW/choice")

        # for repo in self.object.get_user().get_repos():
        #     print(repo.name)

        # header = {"Accept": "application/vnd.github+json", "Authorization": f"Bearer {self.token}"}
        # contentIs = {"message":"my commit message","committer":
        #             {"name":"RASWQQW","email":"RASWQQW@github.com"},
        #             "content":"bXkgbmV3IGZpbGUgY29udGVudHM="}

        # # response = requests.get("https://api.github.com/repos/RASWQQW/CL/branches/main", headers=header)
        # response = requests.put("https://api.github.com/repos/RASWQQW/CL/contents/files/test.txt", 
        #                         data = contentIs,
        #                         headers=header)
        # pprint.pprint(response.json())
        ...

if __name__ == "__main__":
    GitApi().update()