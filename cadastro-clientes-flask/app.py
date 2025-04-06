from flask import Flask, render_template, request, redirect
app = Flask(__name__)

clientes = []

@app.route("/")
def index():
    return render_template("index.html", clientes=clientes)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    clientes.append(nome)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
