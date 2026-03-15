import streamlit as st
from pypdf import PdfReader

# إعدادات الصفحة عشان تطلع مرتبة في الجوال
st.set_page_config(page_title="Mecha Expert", layout="centered")

# تنسيق CSS عشان يمنع تداخل الكلام ويخلي الخط مناسب للجوال
st.markdown("""
    <style>
    body { direction: RTL; text-align: right; }
    [data-testid="stSidebar"] { width: 250px !important; }
    .stMarkdown { font-size: 16px; line-height: 1.6; }
    h1 { font-size: 22px !important; color: #0078D7; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 مستشار الميكاترونكس")

# مساحة رفع الملف (تظهر في البداية بدل ما تكون مخفية وتلخبط خويك)
uploaded_file = st.file_uploader("ارفع المذكرة (PDF) هنا 👇", type="pdf")

if uploaded_file:
    if "text" not in st.session_state:
        with st.spinner("جاري قراءة المذكرة..."):
            reader = PdfReader(uploaded_file)
            st.session_state.text = " ".join([page.extract_text() for page in reader.pages])
        st.success("✅ المذكرة جاهزة للتحليل")

    # مكان المحادثة
    if prompt := st.chat_input("اسأل المهندس عن أي شيء في الكتاب..."):
        st.chat_message("user").markdown(prompt)
        
        # هنا بنحط رد "تجريبي" أو نربطه بـ Gemini بسهولة
        with st.chat_message("assistant"):
            st.write("أنا الحين شغال بنظام 'المعاينة'. الكود صار مرتب وجاهز.")
else:
    st.info("يا مهندس، ارفع المذكرة أول عشان أقدر أساعدك.")
