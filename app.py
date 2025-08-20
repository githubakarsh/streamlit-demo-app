import streamlit as st

st.set_page_config(
    page_title="Streamlit demo application",
)


pg = st.navigation([st.Page("Home.py"), st.Page("About.py"), st.Page("Faq.py"),  st.Page("Signup.py"),  st.Page("Login.py"),  st.Page("Chatbot.py")])
pg.run()