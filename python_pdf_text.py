# Importando bibliotecas necessárias
import fitz

# Abrir o arquivo em PDF
with fitz.open('Relação De Livros Já Lidos.pdf') as pdf:
    texto = ''
    
    for pagina in pdf:
        texto += pagina.getText()
        
print(texto) # Apresenta ao usuário o texto extraído do arquivo PDF