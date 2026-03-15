import streamlit as st
from langchain_ollama import OllamaLLM
from pypdf import PdfReader

st.set_page_config(page_title="Engineer Mind AI", layout="wide")

# تنسيق الواجهة
st.markdown("""<style> @import url('https://fonts.googleapis.com/css2?family=Cairo&display=swap');
    html, body, [data-testid="stAppViewContainer"] { direction: RTL; text-align: right; font-family: 'Cairo', sans-serif; }
    </style>""", unsafe_allow_html=True)

st.title("🧠 العقل الهندسي (تحليل وشرح خطوة بخطوة)")

# موديل Llama 3.1 مع إعدادات تسمح بالتحليل (Temperature 0.4)
llm = OllamaLLM(model="llama3.1", temperature=0.4)

with st.sidebar:
    st.header("📂 مكتبة المراجع")
    uploaded_file = st.file_uploader("ارفع المذكرة", type="pdf")
    context = ""
    if uploaded_file:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            context += page.extract_text()
        st.success("✅ تم استيعاب المرجع.")

if prompt := st.chat_input("اسألني سؤالاً هندسياً يحتاج تفكير..."):
    st.chat_message("user").write(prompt)

    # هنا "سر" العقل البشري: تعليمات التحليل
    system_instruction = (
        "أنت دكتور مهندس خبير في الميكاترونكس. لا تنقل الكلام من الكتاب حرفياً. "
        "مهمتك هي: "
        "1. تحليل السؤال وفهمه بعمق. "
        "2. شرح الحل خطوة بخطوة (Step-by-Step). "
        "3. شرح 'المنطق الهندي' خلف كل إجابة (لماذا فعلنا ذلك؟). "
        "4. إذا كان هناك كود أردوينو، اشرح المنطق البرمجي قبل كتابة الكود. "
        "5. استخدم المذكرة كمرجع، ولكن استخدم ذكاءك الهندسي لتبسيط المعلومة."
    )

    query = f"{system_instruction}\n\nالمرجع المتاح:\n{context[:5000]}\n\nسؤال الطالب: {prompt}"

    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير والتحليل..."):
            response = llm.invoke(query)
            st.write(response)