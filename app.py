from flask import Flask, request,make_response
import json
import os
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/webhook",methods=['POST'])

def lunchparse():
    url = "http://pungduck.hs.kr/lunch.view?date="+"2018"+"08"+"14"
    r = requests.get(url)
    c = r.content
    html = BeautifulSoup(c,"html.parser") #html 파싱
    #print(html)
    menu = html.find("div",{"class":"menuName"})
    #print(menu)
    try:
        span = menu.find("span")
        print(span.text)
        return span.text #메뉴출력
    except:
        return "급식이 없어 "
        
def makeWebhookResult(req):
    if req.get("result").get("action") != 'lunch':
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("lunch")
    speech = lunchparse()
    #print("Respose:")
    print(speech)
    return {
        "speech":speech,
        "displayText":speech,
        "source":"clipai"
    }

def webhook():
    req = request.get_json(silent=True, force=True)
    res = makeWebhookResult(req)
    print(res)
    res = json.dumps(res,indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type']= 'application/json'
    return r

if __name__ == "__main__":
    app.run()
