from project import app, socketio


if __name__ == "__main__":
    print("TV Running")
    socketio.run(app, port=5002)