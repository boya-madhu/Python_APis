print("Hello World!!!")

from flask import Flask

app=Flask(__name__)

@app.route("/")
def APIS():
    return "This is python APIS"

if __name__=='__main__':
    app.run()
