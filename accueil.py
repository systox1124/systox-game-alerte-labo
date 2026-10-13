import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from escape_mobile import show_escape_mobile
from escape import escape as show_escape


width = streamlit_js_eval(
    js_expressions="window.innerWidth",
    key="WIDTH"
)
mobile = width is not None and width < 768

if mobile:
    show_escape_mobile()
else:
    show_escape()