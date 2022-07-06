from flask import Flask, render_template, request
from requestscript import summarize
from BDD/connection import User, engine, read_DB

app = Flask(__name__)				# instantiation application

@app.route('/about')				# association d’une route (URL) avec la fonction suivante
def func_about():
    return render_template('about.html')

@app.route('/home')
def func_home():
    return render_template('home.html')

@app.route('/data', methods = ['GET'])
def func_data():
    return read_DB(engine)

@app.route('/contact')
def func_contact():
    return render_template('contact.html')

@app.route('/contacted', methods = ['GET','POST'])
def func_contacted():
    result = request.form
    n = result['nom']
    e = result['mail']
    t = result['telephone']
    m = result['message']
    utilisateur=User(name=n, email=e, phone=t, message=m)
    utilisateur.to_postgres(engine)
    return render_template("contacted.html", name=n, email=e, phone=t, message=m)

@app.route('/NLP', methods=['POST','get'])
def summary():
    text = request.form.get('msg')
    print(text)
    return summarize(text=text)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5010, debug=True)

