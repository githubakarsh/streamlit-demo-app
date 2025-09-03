import runpy
import streamlit as st
from floating_sidebar import floating_sidebar

st.set_page_config(page_title="Streamlit demo application")

# Map display names to page file paths for the sidebar component
page_map = {
    "Architecture Drift": "pages/dashboard/ArchitectureDrift.py",
    "HLDD Generation": "pages/design/HLDD_Generation.py",
    "HLDD Upgrade": "pages/design/HLDD_Upgrade.py",
    "HLDD Standard": "pages/review/HLDD_Standard.py",
    "Privileged Access Management": "pages/review/PrivilegedAccess.py",
    "AWS Well Architected": "pages/review/AWS_Well_Architected.py",
    "ADR Insight": "pages/review/ADR_Insight.py",
    "Chat Assistant": "pages/chat/Chatbot.py",
}

page_names = list(page_map.keys())

selection = floating_sidebar(page_names, key="floating_sidebar")

# Execute the selected page script
runpy.run_path(page_map[selection], run_name="__main__")

