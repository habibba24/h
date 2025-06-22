import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# إعداد الاتصال بـ Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/habibba24/h/recoil-463722-3bd66cb8a76b.json", scope)
client = gspread.authorize(creds)

# افتح Google Sheet باستخدام الرابط
sheet_url = "https://docs.google.com/spreadsheets/d/1RFT5RQSCqo1XBPg81yfix_TXVjVq_XzTv9EIeZLlw1M/edit?pli=1&gid=0#gid=0"
sheet = client.open_by_url(sheet_url).sheet1

# إعداد صفحة Streamlit
st.set_page_config(page_title="تصالح؟", page_icon="🤝", layout="centered")

# تسجيل الرد في Google Sheets
def log_response(response):
    now = datetime.now()
    row = [now.strftime("%Y-%m-%d %H:%M:%S"), now.strftime("%H:%M:%S"), response]
    sheet.append_row(row)
    #st.success("✅ تم تسجيل ردك في Google Sheets")

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


