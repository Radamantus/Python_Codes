import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá, Luís Augusto</p>
    <p>Aqui é o código Python</p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'E-mail Automático Python' # Assunto
    msg['From'] = 'luis.mesquita.castro@gmail.com' # Remetente
    msg['To'] = 'username@gmail.com' # Destinatário
    password = 'senha' # Senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    # Credenciais de login para enviar o e-mail
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado') # Confirmar envio