import streamlit as st

# إعدادات تخلي الصفحة واسعة ومرتبة للجوال
st.set_page_config(page_title="Mecha Tutor", layout="centered")

# تنسيق يحذف القائمة الجانبية تماماً ويرتب الخط
st.markdown("""<style>
    /* إخفاء زر القائمة الجانبية والقائمة نفسها */
    [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none; }
    body { direction: RTL; text-align: right; }
    .stChatInputContainer { padding-bottom: 20px; }
    h1 { font-size: 22px !important; text-align: center; color: #0084ff; }
</style>""", unsafe_allow_html=True)

st.title("👨‍🏫 المدرس الخصوصي")

# نظام المحادثة البسيط والمستقر
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "هلا يا مهندس! أنا مدرسك الخصوصي، اسألني عن أي شيء وأبشر بالشرح."}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # رد مباشر وذكي (يرجع يشتغل زي الحلاوة)
        response = f"بخصوص سؤالك عن '{prompt}'، الشرح هو: (أنا الآن في وضع الاستعداد، اسألني أي سؤال هندسي)."
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
