import win32com.client as win32

# Criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# Criar um e-mail
email = outlook.CreateItem(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento / qtde_produtos

# configurar as informações do seu e-mail
# email.To = "fulano@gmail.com; beltrano.email@gmail.com"
email.To = "sicrano@gmail.com"
email.Subject = "E-mail Automático do Python"
email.HTMLBody = f"""
<p>Olá pessoa, aqui é o código Python</p>

<p>O faturamento da loja foi de R${faturamento}</p>
<p>Vendemos {qtde_produtos} produtos</p>
<p>O ticket Médio foi de R${ticket_medio}</p>

<p>Cordialmente,</p>
<p>Código Python</p>
"""

# anexo = "C://Users/luism/Documents/MATLAB/example_file.txt"
# email.Attachments.Add(anexo)

email.Send()
print("Email Enviado")
