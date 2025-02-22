import amino
import os
import json
import threading
import requests
import wget
import heroku3
from time import sleep
key="65e14539-0382-408c-9797-379be7ddcdaf"
nickname="your nickname"
app_name="code"
url="https://code.nickname.repl.co"
password="your password"

# Na linha 24 você tem que colocar um deviceid onde indicado
# On line 24 you have to put a deviceid where indicated

print("accgen on")

def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
def send(data):
    requests.post(f"{url}/save",data=data)
client=amino.Client("")

def codee(link):
    return requests.post("https://api-accgen.herokuapp.com", data={"text": link}).json()['captcha']

#password=custompwd


for i in range(3):    
  dev=client.devicee()
  #dev=client.device_id
  email=client.gen_email()
  sleep(12)
  print(email)
  try:
    client.request_verify_code(email = email,dev=dev)
    link=client.get_message(email)
  except Exception as b:
    print(b)
    restart()     
  try: code=codee(link)
  except: pass  
  
  
  try:
    client.register(email = email,password = password,nickname =nickname, verificationCode = code,deviceId=dev)
    #sub.send_message(chatId=chatId,message="Criada")
    d={}
    d["email"]=str(email)
    d["password"]=str(password)
    d["device"]=str(dev)
    t=json.dumps(d)
    data={"data":t}
    send(data)
  except Exception as l:
    print(l)
    pass

restart()
