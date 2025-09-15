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

    _selected_section = on_hover_tabs(menu_data=menu_data, key="main_nav_tabs")


# Adjust the following logic based on what is printed by the debug statement above.
# For example, if _selected_section is a string like "Architecture Drift", use that in your checks.

# 






if _selected_section is None:
    st.title("Welcome to the Streamlit Demo Application")
    st.write("Please select a section from the sidebar to get started.")
if _selected_section == "Architecture Drift":
    import pages.dashboard.ArchitectureDrift as architecture_drift
    architecture_drift.main()
elif _selected_section == "HLDD Generation":
    import pages.design.HLDD_Generation as hldd_generation
    hldd_generation.main()
elif _selected_section == "HLDD Upgrade":
    import pages.design.HLDD_Upgrade as hldd_upgrade
    hldd_upgrade.main()
elif _selected_section == "HLDD Standard":
    import pages.review.HLDD_Standard as hldd_standard
    hldd_standard.main()
elif _selected_section == "Privileged Access Management":
    import pages.review.PrivilegedAccess as privileged_access
    privileged_access.main()
elif _selected_section == "AWS Well Architected":
    import pages.review.AWS_Well_Architected as aws_well_architectured
    aws_well_architectured.main()
elif _selected_section == "ADR Insight":
    import pages.review.ADR_Insight as adr_insight
    adr_insight.main()
elif _selected_section == "Chat Assistant":
    import pages.chat.Chatbot as chat_page
    chat_page.main()
