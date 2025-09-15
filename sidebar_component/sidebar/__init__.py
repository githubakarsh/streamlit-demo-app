import os
import streamlit as st
import streamlit.components.v1 as components

_RELEASE = True

if _RELEASE:

    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _on_hover_tabs = components.declare_component(
        "on_hover_tabs",
        path = build_dir
    )

else:
    _on_hover_tabs = components.declare_component(
    "on_hover_tabs",
    url="http://localhost:3001"
    )

def on_hover_tabs(menu_data, styles=None, default_choice=0, key=None):
    """Render the on-hover sidebar tabs with optional child items.

    Args:
        menu_data (list[dict]): List of dictionaries defining each parent tab.
            Each dictionary requires ``label`` and ``icon`` keys and may include
            a ``children`` key with a list of similar dictionaries for child
            items.
        styles (dict, optional): Optional style overrides passed to the
            component. Defaults to ``None``.
        default_choice (int, optional): Index of the menu item to select by
            default. Defaults to ``0``.
        key (str, optional): Streamlit component key. Defaults to ``None``.

    Returns:
        str: The label of the selected menu item.
    """

    default_label = menu_data[default_choice]["label"] if menu_data else ""

    component_value = _on_hover_tabs(
        menuData=menu_data, styles=styles, key=key, default=default_label
    )

    return component_value

if not _RELEASE:
    st.subheader("Component that creates tabs corresponding with on hover sidebar")
    st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True) # Load the on hover side bar css file



    with st.sidebar:
         demo_menu = [
             {"label": "Dashboard", "icon": "dashboard"},
             {"label": "Money", "icon": "money"},
             {"label": "Economy", "icon": "economy"},
         ]
         tabs = on_hover_tabs(menu_data=demo_menu, key="1")  ## create tabs for on hover navigation bar

    if tabs == 'Dashboard':
        st.title("Navigation Bar")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Money':
        st.title("Paper")
        st.write('Name of option is {}'.format(tabs))

    elif tabs == 'Economy':
        st.title("Tom")
        st.write('Name of option is {}'.format(tabs))
