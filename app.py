from flask import Flask,request
import requests
app=Flask(__name__)

@app.route('/')
def lala():
    return "helloben"
@app.route("/lala",methods=["POST"])
def get():
    url="https://httptest1977.herokuapp.com/lala"
    re=requests.post(url)
    print('re.url',re.url)
    print('@@@re.text###',re.text)
    print('@@@re.content@@@',re.content)

if __name__=='__main__':
    app.run()