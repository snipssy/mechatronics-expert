import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mecha Tutor", layout="centered")

# تنسيق الجوال
st.markdown("""<style>
    body { direction: RTL; text-align: right; }
    .stChatMessage { font-size: 16px; border-radius: 10px; }
    h1 { color: #0084ff; text-align: center; font-size: 20px !important; }
</style>""", unsafe_allow_html=True)

st.title("👨‍🏫 المدرس الخصوصي الذكي")

api_key = st.sidebar.text_input("أدخل مفتاح Google API", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استخدمنا نسخة latest لضمان عدم حدوث خطأ NotFound
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("اسألني عن أي شيء في الميكاترونكس..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # طلب الشرح المفصل
                full_prompt = f"أنت مدرس خصوصي خبير ومحفز. اشرح بأسلوب تعليمي مفصل مع أمثلة عملية: {prompt}"
                response = st.session_state.chat.send_message(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"حدث خطأ في الاتصال: {e}")
else:
    st.info(" في القائمة الجانبية حط API.")
