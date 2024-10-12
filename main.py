from flask import Flask, render_template, jsonify, request
import sender_mail
import base64
import configparser

parser = configparser.ConfigParser()
parser.read("config.properties")

USERNAME = parser["autorizacao"]["username"]
PASSWORD = parser["autorizacao"]["password"]

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


@app.route("/enviaEmail", methods=["POST"])
def send_email():
    """Essa função tem o objetivo Fazer o envio do email."""
    dados = request.get_json()

    # Processar os dados
    assunto = dados["assunto"]
    nome = dados["nome"]
    email = dados["email"]
    telefone = dados["telefone"]
    texto = dados["texto"]
    tipo_contato = dados["tipo_contato"]

    corpo = {
        "tipo_contato": tipo_contato,
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "texto": texto,
    }

    print(corpo)

    send = sender_mail.enviar_email(email, assunto, corpo)

    return send_response(send)


@app.before_request
def before_request():
    """Metodo para validar se a requisição está autorizada"""
    # Verifique se a solicitação inclui um cabeçalho Authorization
    if request.method == "POST":
        auth = request.headers.get("Authorization")
        if auth is None:
            return unauthorized_response()

        # Decodifica o cabeçalho Authorization
        auth_decoded = base64.b64decode(auth.split(" ")[1])

        # Compara a string decodificada com os nomes de usuário e senhas permitidos
        username, password = auth_decoded.decode("utf-8").split(":")

        if username == USERNAME and password == PASSWORD:
            print("Autenticação Validada")
            return

        # Retorna um erro de autenticação
        return unauthorized_response()


def unauthorized_response():
    """Função que valida a chamada"""
    resposta = jsonify({"mensagem": "Não autorizado"})
    resposta.status_code = 401
    return resposta


def send_response(x):
    """Função que valida a chamada"""
    if x is True:
        resposta = jsonify({"mensagem": "Mensagem enviada", "status": "sucesso"})
        resposta.status_code = 200
        return resposta
    else:
        resposta = jsonify({"mensagem": "Erro ao enviar mensagem", "status": "erro"})
        resposta.status_code = 500
        return resposta


@app.route("/busca_prop")
def retorna_propertie():
    "Metodo retorna as propriedades do backend"
    resposta = jsonify({"valor1": USERNAME, "valor2": PASSWORD})
    return resposta


if __name__ == "__main__":
    app.run(debug=True)  # <-- Modo Debug
