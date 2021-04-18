from flask import Flask, render_template
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def inicio():
    nombre = "Carlos Manuel"
    return render_template("inicio.html",nombre=nombre)

app.run("0.0.0.0",5000,debug=True)