from flask import Flask, render_template,request
import math

app=Flask(__name__)

@app.route("/") #decorador o ruta
def index():
    titulo="Pagina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template("index.html", titulo=titulo, listado=listado)

@app.route("/operasbas", methods=["GET","POST"])
def operasbas():
    n1=0
    n2=0
    res=0
    op_txt=''
    simbolo=''
    if request.method == 'POST':
        n1=request.form.get('n1') or 0
        n2=request.form.get('n2') or 0
        op_seleccion = request.form.get('operacion')
        if op_seleccion == 'sumar':
            res = float(n1) + float(n2)
            op_txt = 'suma'
            simbolo = '+'
        elif op_seleccion == 'restar':
            res = float(n1) - float(n2)
            op_txt = 'resta'
            simbolo = '-'
        elif op_seleccion == 'multiplicar':
            res = float(n1) * float(n2)
            op_txt = 'multiplicación'
            simbolo = 'x'
    return render_template('operasbas.html', n1=n1, n2=n2, res=res, operacion=op_txt, simbolo=simbolo)

@app.route("/distancia", methods=["GET","POST"])
def distancia():
    x1=0
    y1=0
    x2=0
    y2=0
    disRes=0
    if request.method == 'POST':
        x1 = float(request.form.get('x1') or 0)
        y1 = float(request.form.get('y1') or 0)
        x2 = float(request.form.get('x2') or 0)
        y2 = float(request.form.get('y2') or 0)
        disRes = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

    return render_template('distancia.html', x1=x1, y1=y1, x2=x2, y2=y2, disRes=disRes)

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