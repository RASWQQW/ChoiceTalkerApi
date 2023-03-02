import json

import pymongo
from conf import username, password
from bson.objectid import ObjectId
from googletrans import Translator

translator = Translator()

class ApiClient(object):
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://talkerdb.mrbr4k4.mongodb.net/myFirstDatabase",
            username=username,
            password=password)

    def insert(self):
        with open("nlp_data4.json", "r") as f:
            listOf = json.load(f)

        for i in range(25071, len(listOf)):
            print(listOf[i])

        # db = self.client.talkerBase
        # PostIn = db.words

        # for elems in listOf:
        #     PostIn.insert_one({
        #         'word_id': pymongo.ASCENDING,
        #         'question': translator.translate(str(elems['question']), dest='kk').text,
        #         'answer': translator.translate(str(elems['answer']), dest='kk').text,
        #         'description': elems['description']
        #     })

        pass

    def getter(self):
        db = self.client.talkerBase
        wordsIs = db.words

        print(wordsIs.find_one())

ApiClient().insert()

