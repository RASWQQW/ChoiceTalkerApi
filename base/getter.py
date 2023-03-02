import pymongo
from base import ApiClient

class Getter(ApiClient):
    def __init__(self):
        super().__init__()

    def getter(self):
        db = self.client.talkerBase
        collectionIs = db.words

        """Write relatively code review for getting relative respond"""


Getter().getter()