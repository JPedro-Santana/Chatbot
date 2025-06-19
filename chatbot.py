from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

respostas = {
    "saldo": "Para ver seu saldo, abra o aplicativo do banco e toque em 'Conta' ou 'Saldo'.",
    "pix": "Para fazer um Pix, vá em 'Pix', escolha o contato e digite o valor.",
    "boleto": "Para pagar um boleto, vá em 'Pagamentos' e escaneie o código de barras.",
    "senha": "Nunca compartilhe sua senha com ninguém.",
    "cartão": "Se perdeu seu cartão, vá em 'Bloquear cartão' no app ou ligue para o banco."
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensagem = data.get("mensagem", "").lower()
    for chave, resposta in respostas.items():
        if chave in mensagem:
            return jsonify({"resposta": resposta})
    return jsonify({"resposta": "Desculpe, não entendi. Você pode perguntar sobre saldo, Pix, boleto ou cartão."})

if __name__ == "__main__":
    app.run(debug=True, port=5000)