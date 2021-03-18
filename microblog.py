from flask import Flask

app = Flask("microblog")

@app.route("/")  # O route pega o app e liga com a função que tá embaixo
def index():
    return "Olá mundo"

app.run()