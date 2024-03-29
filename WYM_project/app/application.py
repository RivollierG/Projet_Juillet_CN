from flask import Flask, render_template, request
from app.model.requestscript import summarize
from app.BDD.connection import User, engine, read_DB_users, Texte, read_DB_texts
from app.BDD.creation import table_creation_texts, table_creation_users
import time
app = Flask(__name__)  ## instantiation application

@app.route('/')
def func_home():
    return render_template('home.html')

@app.route('/about')
def func_about():
    return render_template('about.html')

@app.route('/data', methods = ['GET'])
def func_data():
    list_dict = eval(read_DB_users(engine))
    texte = str()
    for ligne in list_dict:
        l = str("<tr><td>") + str(ligne["id"]) + str("</td><td>") + str(ligne["name"]) + str("</td><td>") + str(ligne["email"]) + str("</td><td>") + str(ligne["phone"])  + str("</td><td>") + str(ligne["message"]) + str("</td></tr>")
        texte = texte + l    
    return render_template("data.html", texte=texte)

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

@app.route('/text', methods = ['GET','POST'])
def func_text():
    return render_template("text.html")

@app.route('/NLP', methods=['POST','GET'])
def summary():
    text = request.form.get('msg')
    now  = time.time()
    resum = summarize(text=text)
    delay = now - time.time()
    print(text)
    monTexte = Texte(contenu=text, resume=resum, date=time.ctime(time.time()), delay = delay)
    monTexte.to_postgres(engine)
    print(read_DB_texts(engine))
    return render_template('NLP.html', texte= resum)

def main():
    table_creation_users(engine)
    table_creation_texts(engine)
    app.run(host='0.0.0.0', port=5010) # démarrage de l’appli

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5010, debug=True)

