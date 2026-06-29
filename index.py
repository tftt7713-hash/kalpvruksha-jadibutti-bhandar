import streamlit as st
import streamlit.components.v1 as components

# Web page ki basic settings (Title aur Full Screen Layout)
st.set_page_config(page_title="My AI Chatbot", layout="wide")

# 1. APNI LINK SIRF IS EK JAGAH PAR UPDATE KAREIN:
CHATBASE_LINK = "PASTE_YOUR_CHATBASE_IFRAME_LINK_HERE"

# 2. HTML styling aur iframe code (Isme koi badlav nahi karna hai)
html_code = f"""
<style>
    body, html {{ 
        margin: 0; 
        padding: 0; 
        height: 100vh; 
        overflow: hidden; 
        background-color: #f4f4f5; 
    }}
    iframe {{ 
        width: 100%; 
        height: 100vh; 
        border: none; 
    }}
</style>
<iframe src="{CHATBASE_LINK}"></iframe>
