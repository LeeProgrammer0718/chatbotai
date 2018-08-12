from flask import Flask, request
import os
app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/webhook",methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = makeWebhookResult(req)
    return "testsuccessful"

if __name__ == "__main__":
    app.run()
