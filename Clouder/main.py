import asyncio
from typing import List
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from Obj.Cupa import Cupa
from bot.BotManager import Manager
import datetime
from datetime import datetime as dt
import random
import os
import sys

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def FirstStep():
    return jsonify({"step1": "Hello Guest how are you?"})


@app.route('/sendVideo/<username>', methods=["GET", "POST"])
def SendVideo(username: str):
    ...

@app.route('/sendPhoto', methods=['GET', 'POST'])
def Home1():
    if request.headers['Username']:
        return Home(request.headers['Username'])
    return jsonify({"error": "Someting wrong with Username header"})

@app.route('/sendPhoto/<username>', methods=['GET', 'POST'])
def Home(username: str):
    # print(request.headers["Content-Type"])
    # print(request.headers['Username'])
    print("All very well!"); print(request.files)
    if request.method == 'POST':
        if 'image' in request.files:
            # print(request.files.getList(), type(request.files.getList()))
            
            file = request.files.get('image'); elIn = file
            gettingpermission = allowed(elIn.filename, type="photo") # check file is have a properly type
            print(gettingpermission)
            if elIn and gettingpermission[0]:
                
                # currentFileName = elIn.filename; #sec_filename = secure_filename(elIn)
                filename = f"{gettingpermission[1][0]}{username}{str(dt.now().strftime('%m.%d.%Y.%S'))}.{gettingpermission[1][1]}" #giving appropriate filename
                # fileIsOn = __file__.replace(os.path.basename(__file__), f"hubCl\\files\\{username}") # saving a file path
                fileIsOn = Cupa().gitpath + f"\\files\\{username}"

                try: os.mkdir(fileIsOn)
                except Exception as e: print(e)
                
                print(f"{fileIsOn}\\{filename}")
                # assert os.path.isfile(f"{fileIsOn}\\{filename}")

                elIn.save(os.path.join(fileIsOn, filename)) # save in git path for adding or commit 
                
                async def main():
                    managerHandling = Manager(executor="bot")
                    await managerHandling
                    return await managerHandling.Sender(
                                        filepath=f"{fileIsOn}\\{filename}",
                                        path=fileIsOn,
                                        filename=filename,
                                        username=username, 
                                        typeIs=gettingpermission[1][1])
                
                manager = asyncio.run(main())
                jsOn = {"link": manager[0], "tg-caption": manager[1]}
                return jsonify(jsOn), 200
                    
    return jsonify({"cond": "not too bad"}), 400


def allowed(filename: str, type:str) -> tuple[bool, list]:
    if type == "photo":
        LIST_OF_FILES = ['png', 'jpeg', 'gif', 'tiff', 'jpg']
        return filename.split(".")[1] in LIST_OF_FILES, filename.split(".")
    if type== "video":
        LIST_OF_FILES = ['video', '']
        return filename.split(".")[1] in LIST_OF_FILES, filename.split(".")



@app.route('/about', methods=['GET', 'POST'])
def index():
    return jsonify({"There is some docs": True})


if __name__ == "__main__":
    app.run(debug=True, port=4755)

