from project import app, socketio


if __name__ == "__main__":
    port = 5002
    print(f"TV Running in {port}")
    socketio.run(app, port=port)
