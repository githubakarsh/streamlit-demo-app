import streamlit as st

st.header("Create event", divider="gray")
st.text_input("Event name", "")
st.number_input("Number of riders ?")


date_col1, date_col2 = st.columns(2)
with date_col1:
    st.date_input("Start date", value=None)
with date_col2:
    st.date_input("End date", value=None)

st.divider()

resetButton, createButton = st.columns(2)
with resetButton:
    st.button("Reset", type="primary", width="stretch")
with createButton:
    st.button("Create event", width="stretch")