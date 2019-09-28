from flask import Flask

app = Flask(__name__)

#App route that will display index.html
@app.route('/')
@app.route('/index')
def about():
    return app.send_static_file('index.html')

if __name__=="__main__":
    app.run(port=80, debug=True)