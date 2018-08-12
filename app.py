from flask import Flask, request
import os
app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/webhook",methods=['POST'])
def makeWebhookResult(req):
    if req.get("result").get("action") != 'lunch':
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("lunch")
    speech = lunchparse(14)
    print("Respose:")
    print(speech)
    return {
        "speech":speech,
        "displayText":speech,
        "source":"clipai"
    }
def webhook():
    req = request.get_json(silent=True, force=True)
    res = makeWebhookResult(req)
    res = json.dumps(res,indent=4)
    return "testsuccessful"

if __name__ == "__main__":
    app.run()
