from flask import Flask, render_template

app = Flask(__name__)

#App route that will display the welcome page
@app.route('/')
@app.route('/about')
def about():
    return render_template('aboutTemplate.html')

#App route to display the resume page
@app.route('/resume')
def resume():
    return render_template('resumeTemplate.html')


if __name__=="__main__":
     app.run()