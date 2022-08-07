import os
import signal

from flask import Flask, request
from db_connector import get_user_by_id

app = Flask(__name__)

@app.route("/users/<user_id>")
def get_user_name(user_id):
 user_name_from_db = get_user_by_id(user_id)
 if user_name_from_db != "":
   return "<H1 id='user'>" + user_name_from_db + "</H1>"
 else:
   return "<H1 id='error'> no such user: " + user_name_from_db + "</H1>"

@app.route('/stop_server')
def stop_server():
 os.kill(os.getpid(), signal.CTRL_C_EVENT)
 return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5001)