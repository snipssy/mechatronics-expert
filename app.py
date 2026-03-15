import streamlit as st
from langchain_groq import ChatGroq
from pypdf import PdfReader

# إعدادات الصفحة لتناسب الجوال
st.set_page_config(page_title="Mecha Mobile", layout="centered")

# CSS احترافي لمنع تداخل الكلام وتصغير الخط في الجوال
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        direction: RTL;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    /* تصغير العناوين في الجوال */
    h1 {
        font-size: 1.5rem !important;
        color: #00FFAA;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    /* تحسين عرض الرسائل */
    .stChatMessage {
        font-size: 14px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 العقل الهندسي")

# إدخال المفتاح (Groq)
api_key = st.sidebar.text_input("Groq API Key", type="password")

if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-70b-versatile")

    if "pdf_text" not in st.session_state:
        st.session_state.pdf_text = ""

    with st.sidebar:
        st.subheader("الملفات")
        uploaded_file = st.file_uploader("ارفع المذكرة", type="pdf")
        if uploaded_file:
            reader = PdfReader(uploaded_file)
            st.session_state.pdf_text = " ".join([page.extract_text() for page in reader.pages])
            st.success("تم!")

    if prompt := st.chat_input("اسأل المهندس..."):
        st.chat_message("user").write(prompt)
        
        # تعليمات الدكتور مهندس المختصرة (عشان النت الضعيف)
        full_query = f"أنت مهندس خبير. المرجع: {st.session_state.pdf_text[:5000]}. السؤال: {prompt}"
        
        with st.chat_message("assistant"):
            response = llm.invoke(full_query)
            st.write(response.content)
else:
    st.info("حط المفتاح في القائمة الجانبية (الزر اللي فوق يسار) عشان نبدأ.")
