import streamlit as st

st.set_page_config(
    page_title="Streamlit demo application",
)


home_page = st.Page("Home.py", title="Home", icon=":material/home:")
about_page = st.Page("About.py", title="About", icon=":material/contact_page:")
faq_page = st.Page("Faq.py", title="Faq", icon=":material/help:")

chatbot_page = st.Page("Chatbot.py", title="Chatbot Assistant", icon=":material/chat:")

pages = {
    "Events": [
        st.Page("create_event.py", title="Create event"),
        st.Page("delete_event.py", title="Delete event"),
         st.Page("update_event.py", title="Update event"),
          st.Page("your_events.py", title="Your  events"),
    ],
    "Other": [
       st.Page("Signup.py", title="Signup", icon=":material/login:"),
        st.Page("Login.py", title="Login", icon=":material/login:")
    ],
    "Home" : [home_page],
    "Chatbot" : [chatbot_page],
    "FAQ" : [faq_page],
    "About" : [about_page]
}

# pg = st.navigation([home_page, about_page, faq_page, chatbot_page])
pg = st.navigation(pages)

pg.run()