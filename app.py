from flask import Flask  # Importa a classe Flask do módulo flask

app = Flask(__name__)


 # esse name tem que voltar main que significa que eu estou rodando ele de forma manual


# Criando uma página web inicial
@app.route('/')
def hello_world():   # É oq será exibido na página inicial
    return 'OI Marvin Como voçê está?'

@app.route('/about') # se no web eu colocar /about, ele vai chamar essa função
def about():
    return 'Essa é a página sobre o Marvin, um assistente virtual.'

if __name__ == '__main__':  # Verifica se o arquivo está sendo executado diretamente
    app.run(debug=True)    # O debug serve pra ver as explicações 