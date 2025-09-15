import streamlit as st
from sidebar_component.sidebar import side_nav

st.set_page_config(
    page_title="Streamlit demo application",
)

# Load custom sidebar CSS for the side navigation component
st.markdown(
    '<style>' + open('sidebar_component/sidebar/style.css').read() + '</style>',
    unsafe_allow_html=True,
)

# Define Streamlit pages for navigation
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

pages = {
    "Dashboard": [architecture_drift],
    "Design": [hldd_generation, hldd_upgrade],
    "Review": [
        hldd_standard,
        privileged_access,
        aws_well_architectured,
        adr_insight,
    ],
    "Chat": [chat_page],
}

pg = st.navigation(pages)

_selected_section = None
with st.sidebar:
    menu_data = [
        {
            "label": "Dashboard",
            "icon": "dashboard",
            "children": [
                {"label": "Architecture Drift", "icon": "add_box"},
            ],
        },
        {
            "label": "Design",
            "icon": "engineering",
            "children": [
                {"label": "HLDD Generation", "icon": "add_box"},
                {"label": "HLDD Upgrade", "icon": "stat_3"},
            ],
        },
        {
            "label": "Review",
            "icon": "fact_check",
            "children": [
                {"label": "HLDD Standard", "icon": "receipt"},
                {"label": "Privileged Access Management", "icon": "login"},
                {"label": "AWS Well Architected", "icon": "domain"},
                {"label": "ADR Insight", "icon": "trip_origin"},
            ],
        },
        {
            "label": "Chat",
            "icon": "chat",
            "children": [
                {"label": "Chat Assistant", "icon": "chat_bubble"},
            ],
        },
    ]

    _selected_section = side_nav(menu_data=menu_data, key="main_nav_tabs")

page_lookup = {
    "Architecture Drift": architecture_drift,
    "HLDD Generation": hldd_generation,
    "HLDD Upgrade": hldd_upgrade,
    "HLDD Standard": hldd_standard,
    "Privileged Access Management": privileged_access,
    "AWS Well Architected": aws_well_architectured,
    "ADR Insight": adr_insight,
    "Chat Assistant": chat_page,
}

if _selected_section:
    page_lookup[_selected_section].run()
else:
    pg.run()
