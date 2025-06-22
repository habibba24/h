import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page config
st.set_page_config(page_title="تصالح؟", page_icon="🤝", layout="centered")

# Excel logging function
def log_response(response):
    log_file = "responses.xlsx"
    full_path = os.path.abspath(log_file)
    #st.write(f"📁 Excel is saved at: {full_path}")  # Shows on the Streamlit app

    now = datetime.now()
    new_row = {
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "time": now.strftime("%H:%M:%S"),
        "response": response
    }
    if os.path.exists(log_file):
        df = pd.read_excel(log_file)
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])
    df.to_excel(log_file, index=False)

# Session state initialization
if 'show_message' not in st.session_state:
    st.session_state['show_message'] = True
if 'response' not in st.session_state:
    st.session_state['response'] = None

# Header styling
st.markdown("""
    <style>
    .center-text {
        text-align: center;
        font-size: 36px;
        color: #444;
        margin-top: 50px;
        margin-bottom: 30px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Show initial prompt
def show_main_message():
    st.markdown('<div class="center-text">ممكن نتصالح؟</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🤝 Okay", use_container_width=True):
            st.session_state['response'] = True
            st.session_state['show_message'] = False
            log_response("Okay")
            st.rerun()
    with col2:
        if st.button("❌ No", use_container_width=True):
            st.session_state['response'] = False
            st.session_state['show_message'] = False
            log_response("No")
            st.rerun()

# Show result after user responds
def show_response():
    if st.session_state['response']:
        st.success(" i miss you ,كلمني بقى يا أبو زين ❤️")
        st.balloons()
    else:
        st.warning("طب فكر تاني .. 😔")
        st.markdown("---")
        if st.button("ارجع تاني يا شاطر"):
            st.session_state['show_message'] = True
            st.session_state['response'] = None
            st.rerun()

# Logic control
if st.session_state['show_message']:
    show_main_message()
else:
    show_response()


