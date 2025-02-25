from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello Feby how are you doing !!!!!'

app.run(debug=True)