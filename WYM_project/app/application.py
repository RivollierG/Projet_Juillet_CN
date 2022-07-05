from flask import Flask, render_template, request
# from BDD/connection import User, engine

app = Flask(__name__)				# instantiation application

@app.route('/about')				        # association d’une route (URL) avec la fonction suivante
def hello(name1="Renaud"):
    return render_template('index.html', name=name1)

@app.route('/contact', methods = ['GET','POST'])
def func_contact():
    result = request.form
    n = result['nom']
    e = result['mail']
    t = result['telephone']
    m = result['message']
    utilisateur=User(name=n, email=e, phone=t, message=m)
    utilisateur.to_postgres(engine)
    return render_template("contacted.html", name=n, email=e, phone=t, message=m)

#hello()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5010, debug=True)

