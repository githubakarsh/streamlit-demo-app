import streamlit as st
from floating_sidebar import floating_sidebar

st.set_page_config(
    page_title="Streamlit demo application",
)

architecture_drift = st.Page(
    "pages/dashboard/ArchitectureDrift.py",
    title="Architecture Drift",
    icon=":material/add_box:",
)

hldd_generation = st.Page(
    "pages/design/HLDD_Generation.py",
    title="HLDD Generation",
    icon=":material/add_box:",
)
hldd_upgrade = st.Page(
    "pages/design/HLDD_Upgrade.py",
    title="HLDD Upgrade",
    icon=":material/stat_3:",
)

hldd_standard = st.Page(
    "pages/review/HLDD_Standard.py",
    title="HLDD Standard",
    icon=":material/receipt:",
)
privileged_access = st.Page(
    "pages/review/PrivilegedAccess.py",
    title="Privileged Access Management",
    icon=":material/login:",
)
aws_well_architectured = st.Page(
    "pages/review/AWS_Well_Architected.py",
    title="AWS Well Architected",
    icon=":material/domain:",
)
adr_insight = st.Page(
    "pages/review/ADR_Insight.py",
    title="ADR Insight",
    icon=":material/trip_origin:",
)

chat_page = st.Page(
    "pages/chat/Chatbot.py",
    title="Chat Assistant",
    icon=":material/chat_bubble:",
)

# Map display names to Page objects for the sidebar component
page_names = [
    "Architecture Drift",
    "HLDD Generation",
    "HLDD Upgrade",
    "HLDD Standard",
    "Privileged Access Management",
    "AWS Well Architected",
    "ADR Insight",
    "Chat Assistant",
]
pages = [
    architecture_drift,
    hldd_generation,
    hldd_upgrade,
    hldd_standard,
    privileged_access,
    aws_well_architectured,
    adr_insight,
    chat_page,
]
page_map = dict(zip(page_names, pages))

selection = floating_sidebar(page_names, key="floating_sidebar")

page_map[selection].run()

