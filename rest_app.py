import json
import os
import signal

from flask import Flask, request
from db_connector import get_user_by_id,add_user_to_table,update_user_name,delete_user_by_id,get_first_free_id

app = Flask(__name__)

# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        user_name_from_db = get_user_by_id(user_id)
        if user_name_from_db != "":
          return  '{“status”: “ok”, “user_name”: '+ user_name_from_db +'}"' , 200
        else:
          return '{“status”: “error”, “reason”: ”no such id”}', 500

    elif request.method == 'POST':
        # getting the json data payload from request
        js = json.loads(request.json)
        user_name = js['name']
        print("in rest_app user_name=" + user_name)
        rc = add_user_to_table(user_name,user_id)
        if rc == 0:
            return '{“status”: “ok”, “user_added”: "'+ user_name +'"}', 200
        else:
            return '{“status”: “error”, “reason”: ”id already exists”}' , 500

    elif request.method == 'PUT':
        # getting the json data payload from request
        js = json.loads(request.json)
        user_name = js['name']
        print("in rest_app user_name=" + user_name)
        rc = update_user_name(user_name,user_id)
        if rc == 0:
            return '{“status”: “ok”, “user_updated”: "'+ user_name +'"}', 200
        else:
            return '{“status”: “error”, “reason”: ”no such id OR id already have this name”}' , 500

    elif request.method == 'DELETE':
        rc = delete_user_by_id(user_id)
        if rc == 0:
            return '{“status”: “ok”, “user_deleted”: "'+ user_id +'"}', 200
        else:
            return '{“status”: “error”, “reason”: ”no such id”}' , 500

#### this method is for Extras 5
@app.route('/users/v2/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user_v2(user_id):
    if  request.method == 'POST':
        # getting the json data payload from request
        js = json.loads(request.json)
        user_name = js['name']
        print("in rest_app user_name=" + user_name)
        rc = add_user_to_table(user_name,user_id)
        if rc == 0:
            return '{“status”: “ok”, “user_added”: "'+ user_name +'"}', 200
        else:
            free_id = get_first_free_id()
            rc = add_user_to_table(user_name, free_id)
            return '{“status”: “ok”, “user_added”: "'+ user_name +' ID: '+free_id+'}', 200

@app.route('/stop_server')
def stop_server():
 os.kill(os.getpid(), signal.CTRL_C_EVENT)
 return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)