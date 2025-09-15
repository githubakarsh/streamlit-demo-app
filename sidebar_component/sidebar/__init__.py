import os
import streamlit as st
import streamlit.components.v1 as components

_RELEASE = True

if _RELEASE:

    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _side_nav = components.declare_component(
        "side_nav",
        path=build_dir,
    )

else:
    _side_nav = components.declare_component(
        "side_nav",
        url="http://localhost:3001",
    )

def side_nav(menu_data, styles=None, default_choice=0, key=None):
    """Render the custom side navigation with optional child items.

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

    component_value = _side_nav(
        menuData=menu_data, styles=styles, key=key, default=default_label,
    )

    return component_value

