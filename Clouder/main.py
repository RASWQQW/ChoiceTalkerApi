import asyncio
from typing import List
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
from testFor import Manager
import datetime
from datetime import datetime as dt
import random
import os
import sys

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def FirstStep():
    return jsonify({"step1": "Hello Guest how are you?"})


@app.route('/sendPhoto/<username>', methods=['GET', 'POST'])
def Home(username: str):
    # print(request.headers["Content-Type"])
    print(request.headers['Username'])
    print("All very well!"); print(request.files)
    if request.method == 'POST':
        if 'image' in request.files:
            # print(request.files.getList(), type(request.files.getList()))
            
            file = request.files.get('image'); elIn = file
            gettingpermission = allowedImage(elIn.filename) # check file is have a properly type
            print(gettingpermission)
            if elIn and gettingpermission[0]:
                
                # currentFileName = elIn.filename; #sec_filename = secure_filename(elIn)
                filename = f"{gettingpermission[1][0]}{username}{str(dt.now().strftime('%m.%d.%Y.%S'))}.{gettingpermission[1][1]}" #giving appropriate filename
                fileIsOn = __file__.replace(os.path.basename(__file__), f"hubCl\\files\\{username}") # saving a file path
                
                try: os.mkdir(fileIsOn)
                except Exception as e: print(e)
                
                print(f"{fileIsOn}\\{filename}")
                # assert os.path.isfile(f"{fileIsOn}\\{filename}")

                elIn.save(os.path.join(fileIsOn, filename)) # save in git path to add or commit 
                manager = asyncio.run(
                                    Manager(executor="bot").Sender(
                                        chatIs='cloudeepee', 
                                        filepath=f"{fileIsOn}\\{filename}",
                                        path=fileIsOn,
                                        filename=filename,
                                        username=username, 
                                        typeIs=gettingpermission[1][1])
                                    )

                jsOn = {"link": manager[0], "tg-caption": manager[1]}
                return jsonify(jsOn), 200
                    
    return jsonify({"cond": "not too bad"}), 400
    

def allowedImage(filename: str) -> tuple[bool, list]:
    LIST_OF_FILES = ['png', 'jpeg', 'gif', 'tiff', 'jpg']
    return filename.split(".")[1] in LIST_OF_FILES, filename.split(".")


@app.route('/about', methods=['GET', 'POST'])
def index():
    return jsonify({"There is some docs": True})


if __name__ == "__main__":
    app.run(debug=True, port=4755)

