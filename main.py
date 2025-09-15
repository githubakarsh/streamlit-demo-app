import streamlit as st
from sidebar_component.sidebar import on_hover_tabs

st.set_page_config(
    page_title="Streamlit demo application",
)

# Load custom sidebar CSS for the on-hover tabs component
st.markdown(
    '<style>' + open('sidebar_component/sidebar/style.css').read() + '</style>',
    unsafe_allow_html=True,
)

# Render the custom on-hover sidebar tabs
with st.sidebar:
    _selected_section = on_hover_tabs(
        tabName=['Dashboard', 'Design', 'Review', 'Chat'],
        iconName=['dashboard', 'engineering', 'fact_check', 'chat'],
        key="main_nav_tabs",
    )

architecture_drift = st.Page("pages/dashboard/ArchitectureDrift.py", title="Architecture Drift", icon=":material/add_box:")

hldd_generation = st.Page("pages/design/HLDD_Generation.py", title="HLDD Generation", icon=":material/add_box:")
hldd_upgrade = st.Page("pages/design/HLDD_Upgrade.py", title="HLDD Upgrade", icon=":material/stat_3:")

hldd_standard = st.Page("pages/review/HLDD_Standard.py", title="HLDD Standard", icon=":material/receipt:")
privileged_access = st.Page("pages/review/PrivilegedAccess.py", title="Privileged Access Management", icon=":material/login:")
aws_well_architectured = st.Page("pages/review/AWS_Well_Architected.py", title="AWS Well Architected", icon=":material/domain:")
adr_insight = st.Page("pages/review/ADR_Insight.py", title="ADR Insight", icon=":material/trip_origin:")

chat_page = st.Page("pages/chat/Chatbot.py", title="Chat Assistant", icon=":material/chat_bubble:")


pages = {

    "Dashboard" : [architecture_drift],
    "Design " : [hldd_generation, hldd_upgrade],
    "Review " : [hldd_standard, privileged_access, aws_well_architectured, adr_insight],
    "Chat " : [chat_page]
}



pg = st.navigation(pages)

pg.run()
