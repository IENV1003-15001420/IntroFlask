from flask import Flask, render_template

app=Flask(__name__)

@app.route("/") #decorador o ruta
def index():
    titulo="Pagina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)

@app.route("/hola") #decorador o ruta
def hola():
    return "<h1> Hola PWA - IEVN-1003 </h1>"

#Como pasar parametros por URL

@app.route("/user/<string:nom>") #decorador o ruta
def user(nom):
    return "<h1> Hola Usuario: {} </h1>".format(nom)

@app.route("/numero/<int:n>") #decorador o ruta
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>") #decorador o ruta
def username(id,username):
    return "ID: {} Nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>") #decorador o ruta
def func(n1,n2):
    return "La Suma es: {}".format(n1+n2)


if __name__=="__main__":
    app.run(debug=True)