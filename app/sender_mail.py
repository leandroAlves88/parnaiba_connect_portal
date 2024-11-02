import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser

parser = configparser.ConfigParser()
parser.read("config.properties")

username = parser["email"]["username"]
password = parser["email"]["password"]
to = parser["email"]["to"]


def enviar_email(remetente, assunto, corpo):
    """função responsável por enviar email"""
    corpohtml = body(corpo)
    print(remetente)
    print(assunto)
    print("Corpo texto: ", corpo)
    try:
        # Configurações do servidor SMTP
        servidor_smtp = "smtp.gmail.com"
        porta_smtp = (
            587  # Porta padrão para comunicação segura com TLS (yahoo é 587 ou 465)
        )

        # Credenciais de login
        usuario = username  #
        destinatario = to
        senha = password

        # Configurar a mensagem
        mensagem = MIMEMultipart()
        mensagem["From"] = usuario
        mensagem["To"] = destinatario
        mensagem["Subject"] = assunto

        # Adicionar corpo da mensagem
        mensagem.attach(MIMEText(corpohtml, "html"))

        # Iniciar conexão com o servidor SMTP
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()  # Usar TLS (Transport Layer Security) para segurança

        # Realizar login no servidor SMTP
        servidor.login(usuario, senha)

        # Enviar e-mail
        servidor.sendmail(usuario, destinatario, mensagem.as_string())

        # Fechar a conexão com o servidor SMTP
        servidor.quit()
        print("email enviado com sucesso")
        return True
    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação. Verifique seu usuário e senha.")
    except smtplib.SMTPConnectError:
        print("Erro de conexão. Verifique a configuração do servidor SMTP.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def body(corpo):
    """construção do corpo do email"""
    tipo_contato = corpo["tipo_contato"]
    nome = corpo["nome"]
    email = corpo["email"]
    telefone = corpo["telefone"]
    texto = corpo["texto"]

    mensagem = f"""
    <br>Tipo de Contato: {tipo_contato}</br>
    <br>Nome: {nome}</br>
    <br>Email: {email}</br>
    <br>Telefone: {telefone}</br>
    <br>Texto: {texto}</br>
    """

    return mensagem
