import streamlit as st

st.set_page_config(
    page_title="Streamlit demo application",
)


home_page = st.Page("Home.py", title="", icon=":material/home:")
about_page = st.Page("About.py", title="About", icon=":material/contact_page:")
faq_page = st.Page("Faq.py", title="Faq", icon=":material/help:")

chatbot_page = st.Page("Chatbot.py", title="Chatbot Assistant", icon=":material/chat:")

login_page = st.Page("Signup.py", title="Signup", icon=":material/login:")
signup_page =  st.Page("Login.py", title="Login", icon=":material/login:")

pages = {
    "Home" : [home_page],
    "Events": [
        st.Page("create_event.py", title="Create event"),
        st.Page("delete_event.py", title="Delete event"),
         st.Page("update_event.py", title="Update event"),
          st.Page("your_events.py", title="Your  events"),
    ],
    "Account": [
       login_page, signup_page
    ],
    "Chatbot" : [chatbot_page],
    "Info" : [faq_page, about_page],
}

# pg = st.navigation([home_page, about_page, faq_page, chatbot_page])
pg = st.navigation(pages)

pg.run()