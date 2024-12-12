import streamlit as st
import boto3
import json
import pandas as pd
import requests

session = boto3.Session(profile_name="iaedn")
client = session.client('bedrock-runtime', region_name='us-west-2')



# =========================
# Função para chamada ao AWS Bedrock
# =========================
def call_bedrock_model(messages):
    payload = {
        "messages": [{"role": msg["role"], "content": msg["content"]} for msg in messages],
        "max_tokens": 200000,
        "anthropic_version": "bedrock-2023-05-31",
        "temperature": 1.0,
        "top_p": 0.95,
        "stop_sequences": []
    }

    try:
        response = client.invoke_model_with_response_stream(
            modelId="anthropic.claude-v2",
            body=json.dumps(payload).encode("utf-8"),
            contentType="application/json",
            accept="application/json"
        )
        output = []
        stream = response.get("body")
        if stream:
            for event in stream:
                chunk = event.get("chunk")
                if chunk:
                    chunk_data = json.loads(chunk.get("bytes").decode())
                    if chunk_data.get("type") == "content_block_delta":
                        delta = chunk_data.get("delta", {})
                        if delta.get("type") == "text_delta":
                            output.append(delta.get("text", ""))
        return "".join(output)
    except Exception as e:
        return f"Erro ao chamar o modelo: {str(e)}"

# =========================
# Interface do Chat
# =========================





# URL do logo hospedado online
logo_url = "https://i.imgur.com/sxYtWkc.jpeg"

# Exibindo o logo a partir da URL
# HTML + CSS para centralizar o logo
st.markdown(
    f"""
    <style>
        .centered-logo {{
            display: flex;
            justify-content: center;
        }}
    </style>
    <div class="centered-logo">
        <img src="{logo_url}" width="500">
    </div>
    """,
    unsafe_allow_html=True
)


# Título do app
st.title("Acessível+ - Plataforma de Acessibilidade")

# Descrição
st.markdown("""
Acessível+ é uma plataforma dedicada a fornecer informações precisas sobre a acessibilidade de locais e rotas para pessoas com deficiência.
Aqui, você pode consultar informações sobre rampas, elevadores, transporte público acessível, e muito mais!
""")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    context = """ Bem-vindo! Você está interagindo com o assistente da Acessível+, que é uma plataforma criada para pessoas com deficiência (PcD),
      oferecendo uma forma prática e eficiente de: 
      Avaliar, localizar e compartilhar informações sobre locais acessíveis.
    Consultar rotas adaptadas e acessar dados atualizados sobre acessibilidade em tempo real.
    Nosso objetivo é facilitar o acesso de pessoas com mobilidade reduzida ou necessidades específicas, promovendo uma experiência mais inclusiva e autônoma para todos.

*Prompt*:

Você é o Acessível+, especializado em acessibilidade para pessoas com mobilidade reduzida e com deficiência (PcD). Sua missão é fornecer informações detalhadas e confiáveis sobre a acessibilidade de locais e rotas, sempre com uma comunicação clara, amigável e acolhedora. Use uma linguagem simples, empática e, sempre que apropriado, inclua emojis para tornar a interação mais próxima e acessível.

Seu papel é analisar as informações sobre diferentes locais e destacar as melhores opções de acordo com os seguintes critérios de acessibilidade:

Rampas de acesso
Elevadores
Banheiros adaptados
Estacionamento reservado
Transporte público acessível
Avisos sonoros para pedestres
Acessibilidade para pessoas autistas
Apoio à comunicação não verbal
Sinalização tátil (para deficientes visuais)
Pisos táteis (para facilitar a locomoção de deficientes visuais)
Espaços com largura adequada para cadeirantes e carrinhos de bebê
Informações em braille
Tecnologia assistiva (como sistemas de leitura de tela)
Acessibilidade em áreas de recreação (para crianças com deficiência)
Disponibilidade de auxiliares de apoio (como cuidadores ou intérpretes de Libras)
Iluminação adequada para deficientes visuais
Zonas de descanso e espera acessíveis
Áreas que aceitam cães-guia

Responda usando emojis e linguagem informal
Importante: Mantenha o foco em fornecer informações relevantes sobre acessibilidade. Evite desviar para temas não relacionados ou dar informações incorretas. Seu objetivo é ser uma fonte confiável e útil para quem busca uma experiência mais inclusiva e acessível. """

    st.session_state.chat_history.append({"role": "user", "content": context, "hidden": True})

if 'show_chat_history' not in st.session_state: st.session_state['show_chat_history'] = True

#user_input = st.text_area("Digite sua mensagem ou personalize o prompt:", key="user_input")

# Campo de perguntas com placeholder
user_input = st.text_input("O que você gostaria de saber sobre acessibilidade?", 
                          placeholder="Exemplo: Onde tem rampas de acesso?")
# Instruções para o usuário
st.markdown("""
    **Dúvidas comuns que você pode perguntar:**
    - Onde tem rampas de acesso?
    - Quais locais têm banheiros adaptados?
    - Qual transporte público é acessível na minha região?
    - Há alguma área com sinalização tátil?
""")


def add_message_to_history(role, content, hidden=False):
    if not hidden:
        if not st.session_state.chat_history or st.session_state.chat_history[-1]["role"] != role:
            st.session_state.chat_history.append({"role": role, "content": content})
    else:
        st.session_state.chat_history.append({"role": role, "content": content, "hidden": True})




if st.button("Enviar"):
    if user_input.strip():
        add_message_to_history("user", user_input)

        with st.spinner("Buscando resposta..."):
            model_response = call_bedrock_model(
                [msg for msg in st.session_state.chat_history]
            )

            add_message_to_history("assistant", model_response)

st.subheader("Histórico do Chat")
for message in st.session_state.chat_history:
    if not message.get("hidden", False):
        if message["role"] == "user":
            st.write(f"**Usuário:** {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"**Modelo:** {message['content']}")

# Rodapé com informações de contato (em vermelho)
st.markdown("""
---
#### Acessível+ | Todos os direitos reservados.
💬 Para mais informações, entre em contato conosco através do email: contato@acessivelplus.com
""")