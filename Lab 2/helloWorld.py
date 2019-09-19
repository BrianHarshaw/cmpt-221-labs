from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>If you enter /user in the URL then put your name after that in the URL, you will be directed to your page!</h1>
        <a href=" http://127.0.0.1:5000/about">Our About Page</a>
    </body>
</html>'''

@app.route('/about')
def about():
    return '''
        <p> 
            <ol>
                <li>Flask is a really cool web framework that is used in Python</li>
                <li>It doesn't come with much to it, but that just makes it highly customizable</li>
                <li>The way that Flask navigates your web page is by using routes</li>
                <li>A route is used to run certain functions, based on what is in the URL</li>
                <li>Static routes are routes that do not change and have set URL's</li>
                <li>Dynamic routes accept parameters and can change based on the user's input</li>
            </ol>
        </p>
    '''

@app.route('/user/<username>')
def show_post(username):
    return '''
    <html>
        <body>
            <h1>Hello '''+ username +''', I have a poem for you!</h1>
            <p>
                Flask is fun, Python is too, But please give us less, Homework to do  
            </p>
        </body>
    </html>
    '''


if __name__=="__main__":
     app.run()