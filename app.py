from flask import Flask,request
import requests
app=Flask(__name__)

@app.route('/')
def lala():
    return "helloben"
@app.route("/lala",methods=["GET"])
def get():
    url="http://127.0.0.1:5000/lala"
    re=requests.get(url)
    print(re.url)
    print(re.text)
    print(re.content)


app.run()