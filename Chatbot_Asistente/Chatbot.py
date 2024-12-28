import os
import openai
import streamlit as st

# Clave de API de OpenAI
with open('/keys/key_api1.txt') as f:
   openai.api_key = f.readline()

# Título de la aplicación
st.title("_Asistente Virtual_ :smile:")

# Historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mensaje inicial si no hay historial de mensajes
if not st.session_state.messages:
    st.markdown(
        """
        ### ¡Bienvenido!
        Este chatbot está diseñado para ayudarte a resolver cualquier consulta que tengas.
                
        Escribe tu mensaje en el campo a continuación para comenzar. 😊
        """
    )

# Visualización de Historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada de texto y botón de envío
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Agregagmos el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta del chatbot
    with st.chat_message("assistant"):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": """Eres un Asistente virtual de una empresa dedicada a la venta de inmuebles. En cada respuesta se amigable y muestrate encantado de ayudar.
                 Si es la primera vez que te realizan una consulta presentate y ofrece tus servicios"""},
                *st.session_state.messages
            ],
            temperature=0.5
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
        # Agrega la respuesta del chatbot al historial
        st.session_state.messages.append({"role": "assistant", "content": answer})