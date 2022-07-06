from flask import Blueprint, Flask, render_template
from jinja2 import TemplateNotFound
# from BDD/connection import User, engine

app = Flask(__name__)				# instantiation application

@app.route('/')				        # association d’une route (URL) avec la fonction suivante
def hello_world():
    return 'Hello world!'
def hello(name=None):
    return render_template('index.html', name=name)

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

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5010, debug=True)



simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)
