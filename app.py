from flask import Flask, render_template, abort
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def inicio():
    nombre = "Carlos Manuel"
    return render_template("inicio.html",nombre=nombre)

@app.route('/potencia',methods=["GET","POST"])
def potencia():
    return render_template("potencia.html")

@app.route("/potencia/<base>/<expo>",methods=["GET","POST"])
def operar_potencia (base,expo):
    base = int(base)
    expo = int(expo)
    if expo == 0:
        resultado = 1
    elif expo < 0:
        resultado = 1/(base**-(expo))
    elif expo > 0:
        resultado = base ** expo
    else:
        abort(404)
    return render_template("operar_potencia.html",num1=base,num2=expo,num3=resultado)

@app.route('/cuenta_letras',methods=["GET","POST"])
def cuenta ():
    return render_template("letras.html")

@app.route("/cuenta_letras/<palabra>/<letra>",methods=["GET","POST"])
def cuenta_letra (palabra,letra):
    if len(letra) > 1:
        abort(404)
    else:
        cont = palabra.count(letra)
    
    if cont == 1:
        palabra2 = "vez"
    else:
        palabra2 = "veces"
    return render_template("cuenta_letra.html",pa1=palabra,pa2=letra,pa3=palabra2,resu=cont)

app.run("0.0.0.0",5000,debug=True)