import eventlet
eventlet.monkey_patch()
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS


app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')
CORS(app)


from .controllers import main_controller
