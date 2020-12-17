from project import app
from project.model.tv_model import TV
from project.util.response import construct_response
from project.communication.client_tv import ClientTV
from flask import request, render_template, send_from_directory, jsonify, send_file
import json
import requests

client_tv = ClientTV()
client_tv.subscribe()


@app.route("/", methods=["GET"])
def check():
    return "I'm working TV"


@app.route("/tv_receive", methods=["POST"])
def receive_sm():
    global client_tv
    if client_tv.block:
        print("Tv's locked")
        data = {"msg": "Tv's locked"}
        client_tv.publish_to_dojot(data)
        return (
            jsonify(construct_response("status", {"info": "Tv's blocked"}, "smp")),
            200,
        )

    else:
        print(f"Receive {json.dumps(request.json, indent=4, sort_keys=True)}")
        print("Tv's unlocked")
        data = {"msg": "Tv's unlocked"}
        client_tv.publish_to_dojot(data)
        return (
            jsonify(construct_response("status", {"info": "Tv's unlocked"}, "smp")),
            200,
        )


@app.route("/change", methods=["POST"])
def change():
    global client_tv
    
    command = request.json["lock"]
    client_tv.status = command

    return (
        jsonify(
            construct_response("status", {"info": f"Tv's status is {client_tv.status}"})
        ),
        200,
    )
