from flask import Flask, request,make_response
import json
import os
import requests
from bs4 import BeautifulSoup
import datetime
app = Flask(__name__)
now = datetime.datetime.now()
#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/webhook",methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = makeWebhookResult(req)
    #print(res)
    res = json.dumps(res,indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type']= 'application/json'
    return r

def lunchparse():
    t = time(now)
    url = "http://pungduck.hs.kr/lunch.view?date="+"2018"+t[1]+t[2]
    r = requests.get(url)
    c = r.content
    html = BeautifulSoup(c,"html.parser") #html 파싱
    #print(html)
    menu = html.find("div",{"class":"menuName"})
    #print(menu)
    try:
        span = menu.find("span")
        lun = span.text
        return lun #메뉴출력
    except:
        return "급식이 없어요!!"
        
def makeWebhookResult(req):
    action = req.get("result").get("action")
    if  action == 'lunch':
        result = req.get("result")
        parameters = result.get("parameters")
        time = parameters.get("date-time")
        speech = lunchparse()
        #print("Respose:")
        #print(speech)
    else:
        return {}

    return {
        "speech":speech,
        "displayText":speech,
        "source":"clipai"
    }

def time(time): #서버가 미국에 있으므로 한국에서 사용하려면 시차계산 필요
    date = [0,1,2,3]
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    khour = hour+9 #한국 시차계산
    kday = day
    kmonth = month
    if khour >24:
        khour = khour-24
        kday +=1
        if month in [1,3,5,7,8,10,12]:
            if kday>31:
                kday = 1
                kmonth +=1
        else:
            if kday>30:
                kday = 1
                kmonth +=1
    if kmonth<10:
        kmonth = '0'+str(kmonth)
    else:
        kmonth = str(kmonth)
    date[0] = str(year)
    date[1] = kmonth
    date[2] = str(kday)
    date[3] = str(khour)
    return date

if __name__ == "__main__":
    app.run()
