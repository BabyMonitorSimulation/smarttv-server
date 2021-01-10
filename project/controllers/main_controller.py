from project import app
from project.model.tv_model import TV
from project.communication.client_tv import ClientTV
from project.util.response import construct_response
from flask import request, render_template, send_from_directory, jsonify, send_file
import json
import requests

smtv = TV("unlocked")
client_tv = ClientTV()


@app.route("/", methods=["GET"])
def check():
    return "I'm working TV"


@app.route("/change_status", methods=["POST"])
def change_status():
    global smtv

    command = request.json["lock"]
    smtv.status = command

    return (
        jsonify(
            construct_response("status", {"info": f"Tv's status is {smtv.status}"})
        ),
        200,
    )


@app.route("/receive-data", methods=["POST"])
def receive_msgs():
    global smtv, client_tv

    print("Received Message")
    data = {
        "msg": smtv.status,
        "from": "tv",
        "to": request.json["from"],
        "type": "status",
    }
    client_tv.publish_to_dojot(data)
    
    return jsonify(data), 200


@app.route("/get_status", methods=["GET"])
def get_status():
    global smtv

    return {"msg": smtv.status}
