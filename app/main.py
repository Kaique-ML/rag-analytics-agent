import streamlit as st
from agent.rag_chain import get_rag_chain
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="RAG Analytics Agent", page_icon="🤖")

st.title("🤖 RAG Analytics Agent")
st.markdown("Pergunte sobre seus dados de vendas em linguagem natural.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ex: Qual foi a receita total no último mês?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chain = get_rag_chain()
        response = chain.invoke(prompt)
        answer = response["result"]
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer}) 