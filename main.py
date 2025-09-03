import streamlit as st
import importlib.util
from pathlib import Path
import sys

from sidebar_component.sidebar_comp import on_hover_tabs

st.set_page_config(
    page_title="Streamlit demo application",
)

# Load the custom sidebar component from the local repository
component_path = Path(__file__).parent / "sidebar-component" / "sidebar-comp" / "__init__.py"
spec = importlib.util.spec_from_file_location("sidebar_tabs", component_path)
sidebar_tabs = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = sidebar_tabs
spec.loader.exec_module(sidebar_tabs)
on_hover_tabs = sidebar_tabs.on_hover_tabs

# Apply the sidebar CSS styles
css_path = Path(__file__).parent / "sidebar-component" / "sidebar-comp" / "style.css"
st.markdown('<style>' + css_path.read_text() + '</style>', unsafe_allow_html=True)

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

# Map display names to Page objects and icons for the sidebar component
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
icons = [
    "add_box",
    "add_box",
    "stat_3",
    "receipt",
    "login",
    "domain",
    "trip_origin",
    "chat_bubble",
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

with st.sidebar:
    selection = on_hover_tabs(tabName=page_names, iconName=icons, default_choice=0)

page_map[selection].run()

