import streamlit as st
import google.generativeai as genai

# إعدادات الواجهة
st.set_page_config(page_title="Mecha Tutor", layout="centered")

st.markdown("""<style>
    body { direction: RTL; text-align: right; }
    .stChatMessage { font-size: 16px; border-radius: 10px; }
    h1 { color: #0084ff; text-align: center; }
</style>""", unsafe_allow_html=True)

st.title("👨‍🏫 المدرس الخصوصي الذكي")

# إدخال المفتاح مرة واحدة (أو حطه في السايد بار)
api_key = st.sidebar.text_input("أدخل مفتاح Google API", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض المحادثة السابقة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("اسألني عن الأردوينو، الحساسات، أو أي شيء..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # تعليمات المدرس الخصوصي
            full_prompt = f"أنت مدرس خصوصي خبير في هندسة الميكاترونكس. اشرح بأسلوب مبسط، تعليمي، وخطوات واضحة. السؤال هو: {prompt}"
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("يا ريان، خل خويك يحط مفتاح الـ API في القائمة الجانبية عشان يبدأ المدرس يشرح.")
