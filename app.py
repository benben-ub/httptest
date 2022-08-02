from flask import Flask,request
import requests
app=Flask(__name__)

@app.route('/')
def lala():
    return "helloben"
@app.route("/lala",methods=["GET"])
def get():
    url="https://httptest1977.herokuapp.com/lala"
    re=requests.get(url)
    print(re.url)
    print(re.text)
    print(re.content)


app.run()