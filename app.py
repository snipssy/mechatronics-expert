import streamlit as st
from langchain_groq import ChatGroq

# إعدادات الصفحة
st.set_page_config(page_title="Mecha Tutor", layout="centered")

# إخفاء القائمة الجانبية وتنسيق الجوال
st.markdown("""<style>
    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none; }
    body { direction: RTL; text-align: right; }
    h1 { font-size: 22px !important; text-align: center; color: #0084ff; }
</style>""", unsafe_allow_html=True)

st.title("👨‍🏫 المدرس الخصوصي الذكي")

# ربط الذكاء (حط مفتاحك هنا مباشرة بين القوسين عشان يشتغل لخويك فوراً)
# أو خليه يطلبه مرة واحدة
api_key = st.text_input("أدخل مفتاح Groq لبدء التفكير:", type="password")

if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.1-70b-versatile")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("اسألني أي شيء في الميكاترونكس..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # هنا "التفكير" الحقيقي
            instruction = "أنت مدرس هندسة ميكاترونكس خبير. اشرح بأسلوب تعليمي مفصل."
            response = llm.invoke(f"{instruction}\n\nالسؤال: {prompt}")
            st.markdown(response.content)
            st.session_state.messages.append({"role": "assistant", "content": response.content})
else:
    st.info("أدخل المفتاح لمرة واحدة فقط لتفعيل 'عقل' المدرس.")
