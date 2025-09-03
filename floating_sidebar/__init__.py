import os
import streamlit.components.v1 as components

_component_func = components.declare_component(
    "floating_sidebar",
    path=os.path.join(os.path.dirname(__file__), "frontend"),
)

def floating_sidebar(items, default=None, key=None):
    if default is None and items:
        default = items[0]
    return _component_func(items=items, default=default, key=key)
