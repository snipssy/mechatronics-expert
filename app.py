import streamlit as st
import requests

st.set_page_config(page_title="Mecha Tutor", layout="centered")

st.markdown("""<style>
    body { direction: RTL; text-align: right; }
    .stChatMessage { font-size: 16px; border-radius: 10px; }
    h1 { color: #0084ff; text-align: center; }
</style>""", unsafe_allow_html=True)

st.title("👨‍🏫 المدرس الخصوصي الذكي")

api_key = st.sidebar.text_input("أدخل مفتاح Google API", type="password")

if api_key:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("اسألني أي شيء في الهندسة..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # مناداة السيرفر مباشرة عبر API v1 (النسخة المستقرة)
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = {
                "contents": [{"parts": [{"text": f"أنت مدرس ميكاترونكس خبير. اشرح بوضوح: {prompt}"}]}]
            }
            
            try:
                response = requests.post(url, json=payload)
                result = response.json()
                
                if "candidates" in result:
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"مشكلة في المفتاح أو الرد: {result}")
            except Exception as e:
                st.error(f"فشل الاتصال: {e}")
else:
    st.info("حط المفتاح في القائمة الجانبية عشان نخلص.")
