"""the is the main app of the bot sever in flask structure

Recieve HTTP get request and analyse it.
Return the next state and the reply of the bot

Using http://127.0.0.1:5000 as a "hello world" to check server running and connect
Using http://127.0.0.1:5000/bot as bot server and must post/get a json with
{state_id : , request_c :}
"""
from flask import Flask
from flask import request
from flask_cors import CORS
    

import json
path = "script\\script.txt"
app = Flask(__name__)
app.debug = True

from parser import load_script
from interpreter import generate
#main bot server,cors:Cross-Origin Resource Sharing
CORS(app, resources=r'/*')
@app.route("/bot",methods=['POST', 'GET'])
def server():
    with open(path, 'r', encoding='utf8') as f:
        script = load_script(f)
    req = request.json    
    answerlist = generate(script, req['state_id'], req['request_c'])
    answerdict = {}
    answerdict['state_id'] = answerlist[0]
    answerdict['reply'] = answerlist[1]
    return answerdict
#test server running and connect
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"