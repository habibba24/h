import streamlit as st
from datetime import datetime
import gspread

# تهيئة Session State
if 'show_message' not in st.session_state:
    st.session_state['show_message'] = True
if 'response' not in st.session_state:
    st.session_state['response'] = None

# تنسيق العنوان
st.markdown("""
    <style>
    .center-text {
        text-align: center;
        font-size: 36px;
        color: #444;
        margin-top: 50px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# عرض الرسالة الأولى
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

# عرض رد الفعل
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

# التحكم في العرض
if st.session_state['show_message']:
    show_main_message()
else:
    show_response()


