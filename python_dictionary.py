# Dicionáros Python
emails_gerentes = {
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "plaza@gmail.com",
    "Barra": "barra@gmail.com,"
}

email = emails_gerentes['Iguatemi']
print(email)

emails_gerentes['Leblon'] = "leblon@gmail.com"
print(emails_gerentes)

# forma 1: fazer um for
for shopping in emails_gerentes:
    print(shopping)

# forma 2: dicionario.keys()
print(emails_gerentes.keys())

# forma 1: fazer um for
for shopping in emails_gerentes:
    print(emails_gerentes[shopping])

# forma 2: dicionarios.values
print(emails_gerentes.values())

emails_gerentes.pop("Leblon")
print(emails_gerentes)

if "Iguatemi" in emails_gerentes:
    print("Tem sim")
else:
    print("Tem não")