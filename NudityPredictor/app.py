from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = PyMongo(app)
socketio = SocketIO(app)

MESSAGES_COLLECTION = "messages"

@app.route("/")
def index():
    return render_template("index.html")  # Assuming your index.html is in a templates folder

@socketio.on("connect")
def handle_connect():
    print("A new client is connected")
    messages = mongo.db[MESSAGES_COLLECTION].find()
    emit("load messages", messages)

@socketio.on("username")
def handle_username(username):
    print(username)
    emit("user joined", username)

@socketio.on("chat message")
def handle_chat_message(msg):
    message = {
        "author": msg["author"],
        "content": msg["content"],
        "image": msg.get("image"),  # Handle potential absence of image
    }
    mongo.db[MESSAGES_COLLECTION].insert_one(message)
    emit("chat message", msg)

@socketio.on("disconnect")
def handle_disconnect():
    username = request.sid  # Example for retrieving username from socket context
    emit("user left", username)

if __name__ == "__main__":
    socketio.run(app, debug=True)
