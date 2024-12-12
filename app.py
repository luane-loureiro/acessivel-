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
st.title("Chat com AWS Bedrock")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    context = """
    O Acessível+ é uma plataforma que conecta e empodera pessoas com deficiência (PcD), permitindo que:
    Avaliem, localizem e compartilhem informações sobre locais  acessíveis.
    Consultem rotas (locais) adaptados e dados atualizados sobre 	acessibilidade em tempo real.
    

    *Prompt*: "Você é um assistente especializado em acessibilidade para pessoas com mobilidade reduzida e CPD.
    Tente responder de maneira mais humanizada e acessível para o usuário, incluindo emojis e usando uma linguagem informal.
      Sua tarefa é analisar as informações fornecidas sobre localidades e identificar as melhores opções 
      com base em critérios de acessibilidade,
        como rampas, elevadores, banheiros adaptados, estacionamento reservado, 
        transporte público acessível, aviso sonoro para pedestres, acessibilidade para autistas, apoio de comunição não verbal
          e outras facilidades voltadas para inclusão."
      ---nao induza o usuario ao erro, falando sobre coisas nao relacionadas ao contexto fornecido.---
      
    
    """
    st.session_state.chat_history.append({"role": "user", "content": context})

if 'show_chat_history' not in st.session_state: st.session_state['show_chat_history'] = True

user_input = st.text_area("Digite sua mensagem ou personalize o prompt:", key="user_input")

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
                [msg for msg in st.session_state.chat_history if not msg.get("hidden", False)]
            )

            add_message_to_history("assistant", model_response)

st.subheader("Histórico do Chat")
for message in st.session_state.chat_history:
    if not message.get("hidden", False):
        if message["role"] == "user":
            st.write(f"**Usuário:** {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"**Modelo:** {message['content']}")

