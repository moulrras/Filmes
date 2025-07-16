from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("cadastro.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    idade = request.form["idade"]

    if nome and email and telefone and idade:
        with open("clientes.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nome, email, telefone,idade])
        return redirect("/")
    else:
        return "Preencha todos os campos!", 400

if __name__ == "__main__":
    app.run(debug=True)
