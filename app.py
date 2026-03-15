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
        # هذا هو المسمى الرسمي والمستقر حالياً
        model = genai.GenerativeModel('gemini-1.5-flash')
        
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
                # طلب الشرح بأسلوب المدرس
                full_prompt = f"أنت مدرس خصوصي خبير. اشرح بأسلوب تعليمي مفصل وخطوات واضحة: {prompt}"
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"تنبيه: تأكد من صحة المفتاح أو جرب لاحقاً. الخطأ: {e}")
else:
    st.info("API في القائمة الجانبية.")
