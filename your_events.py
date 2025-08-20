import streamlit as st

st.header("Your events", divider="gray")


col1, col2, col3 = st.columns(3)
col1.metric("Your events", "12")
col2.metric("Upcoming events", "3")
col3.metric("Cancelled", "14")

st.divider()

for_more_info = '''For more info : '''

st.markdown(for_more_info) 
st.page_link("Home.py", label="Home", icon="🏠")
