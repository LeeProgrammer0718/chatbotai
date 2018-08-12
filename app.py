from flask import Flask, request
import os
app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/")
def receive_message():
    return "testsuccessful"
if __name__ == "__main__":
    app.run()
