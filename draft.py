import streamlit as st


st.title("Part 13: Connections and Secrets")

st.header("1. Connection and Secret Management")
st.write('user', st.secrets.db_username)


st.write(st.secrets.OPENAI_API_KEY)
