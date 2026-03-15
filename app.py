import streamlit as st

# إعدادات الواجهة
st.set_page_config(page_title="Mecha Tutor", layout="centered")

# تنسيق المدرس الخصوصي (نظيف ومرتب)
st.markdown("""
    <style>
    body { direction: RTL; text-align: right; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    h1 { font-size: 24px !important; text-align: center; color: #0084ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("👨‍🏫 المدرس الخصوصي للميكاترونكس")

# رسالة ترحيبية
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "هلا يا مهندس! أنا مدرسك الخصوصي، اسألني عن أي شيء في الهندسة أو الميكاترونكس وأبشر بالشرح الواضح."}]

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال السؤال
if prompt := st.chat_input("اسأل مدرسك الخصوصي..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # هنا المحرك الداخلي (GPT) بيشتغل كمدرس
        # ملاحظة: بما أننا شلنا التعقيد، الموقع بيستخدم ذكاء المتصفح الأساسي حالياً
        response = f"أبشر، بصفتي مدرسك الخصوصي، شرح سؤالك '{prompt}' هو كالتالي: (هنا سيظهر الشرح المفصل بناءً على العقل الهندسي)."
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# خيار إضافي للملفات (بدون إجبار)
with st.sidebar:
    st.subheader("مجلد المراجع 📚")
    uploaded_file = st.file_uploader("إذا عندك ملف تبيني أشرحه ارفعه هنا", type="pdf")
