import streamlit as st

# Configurações de layout
st.set_page_config(page_title="Assistente Bancário", page_icon="💬", layout="centered")

st.markdown("<h1 style='text-align: center; font-size: 36px;'>💬 Assistente Bancário</h1>", unsafe_allow_html=True)
st.write("Olá! Eu sou o seu assistente virtual. Me pergunte algo sobre o aplicativo do banco!")

# Base de respostas simples
respostas = {
    "saldo": "Para ver seu saldo, abra o aplicativo do banco e toque em 'Conta' ou 'Saldo'.",
    "pix": "Para fazer um Pix, vá em 'Pix', escolha o contato e digite o valor. Depois, confirme com sua senha.",
    "transferência": "Para transferir dinheiro, vá em 'Transferência', selecione a conta de destino e digite o valor.",
    "boleto": "Para pagar um boleto, vá em 'Pagamentos', aponte a câmera para o código de barras ou digite os números.",
    "senha": "Nunca compartilhe sua senha com ninguém. Nem mesmo com o banco.",
    "cartão": "Se perdeu seu cartão, entre no app e procure 'Bloquear cartão' ou ligue para o banco imediatamente.",
    "falar com gerente": "Procure a opção 'Ajuda' ou 'Fale conosco' no aplicativo para falar com seu gerente.",
    "ajuda": "Estou aqui para ajudar! Você pode perguntar sobre saldo, Pix, boletos, transferências e mais!"
}

# Entrada do usuário
pergunta = st.text_input("Digite sua dúvida abaixo:")

if pergunta:
    encontrou = False
    for chave in respostas:
        if chave in pergunta.lower():
            st.success(respostas[chave])
            encontrou = True
            break
    if not encontrou:
        st.warning("Desculpe, não entendi sua dúvida. Tente perguntar sobre: saldo, Pix, boleto, segurança, senha ou cartão.")
# Layout dos botões
st.subheader("📌 Perguntas rápidas:")
col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Ver Saldo"):
        st.success(respostas["saldo"])
    if st.button("💸 Fazer Pix"):
        st.success(respostas["pix"])
    if st.button("🏦 Transferência"):
        st.success(respostas["transferência"])
    if st.button("📄 Pagar Boleto"):
        st.success(respostas["boleto"])

with col2:
    if st.button("🔐 Senha"):
        st.success(respostas["senha"])
    if st.button("💳 Perdi o Cartão"):
        st.success(respostas["cartão"])

