import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Mecha Tutor", layout="centered")

# تنسيق الجوال (مرتب ومنظم)
st.markdown("""<style>
    body { direction: RTL; text-align: right; }
    .stChatMessage { font-size: 16px; border-radius: 10px; }
    h1 { color: #0084ff; text-align: center; }
</style>""", unsafe_allow_html=True)

st.title("👨‍🏫 المدرس الخصوصي الذكي")

api_key = st.sidebar.text_input("أدخل مفتاح Google API", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استخدمنا المسمى الأبسط والأضمن
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("اسأل مدرسك الخصوصي..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # طلب الشرح بأسلوب المدرس
                response = model.generate_content(f"أنت مدرس ميكاترونكس خبير. اشرح بوضوح: {prompt}")
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"تأكد من المفتاح. الخطأ: {e}")
else:
    st.info("حط المفتاح في القائمة الجانبية عشان نخلص.")
