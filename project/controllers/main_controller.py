from project import app
from project.model.tv_model import TV
from project.util.response import construct_response
from flask import request, render_template, send_from_directory, jsonify, send_file
import json
import requests

smtv = TV('locked')

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


@app.route("/receive_msgs", methods=["POST"])
def receive_msgs():
    global smtv

    print('Received Message')

    return {'msg': smtv.status}


@app.route("/get_status", methods=["GET"])
def get_status():
    global smtv

    return {'msg': smtv.status}
