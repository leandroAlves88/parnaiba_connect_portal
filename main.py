from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def home():
    """Rota de acesso a pagina a pagina princial."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Rota de acesso a pagina a pagina Sobre."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Rota de acesso a pagina a pagina Entre em Contato."""
    return render_template("contact.html")


@app.route("/painel_dados")
def blog():
    """Rota de acesso a pagina a pagina Blog."""
    return render_template("painel_dados.html")


@app.route("/historia")
def service():
    """Rota de acesso a pagina a pagina Service."""
    return render_template("historia.html")


if __name__ == "__main__":
    app.run(debug=True)  # <-- Modo Debug
