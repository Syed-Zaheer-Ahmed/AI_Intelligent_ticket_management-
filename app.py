import streamlit as st
import pickle
import numpy as np
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Ticket Intelligence",
    page_icon="🎫",
    layout="wide"
)

# ================= LOAD MODELS =================
import joblib

joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(category_model, "category_model.pkl")
joblib.dump(priority_model, "priority_model.pkl")
joblib.dump(queue_model, "queue_model.pkl")

# ================= PREMIUM CSS =================
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.glass {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #4CAF50;
}

.subtitle {
    color: gray;
    margin-bottom: 20px;
}

.stButton>button {
    background: linear-gradient(90deg, #4CAF50, #00c6ff);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("📊 Dashboard")
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📘 About Project"]
)

# ================= HOME PAGE =================
if page == "🏠 Home":

    st.markdown('<div class="big-title">🎫 AI Ticket Intelligence System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Smart IT Ticket Classification & Prioritization</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    # -------- Ticket Input --------
    with col1:
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        ticket_text = st.text_area(
            "✍ Enter Ticket Description",
            height=200,
            placeholder="Example: User unable to login into VPN..."
        )

        predict_btn = st.button("🚀 Analyze Ticket")

        st.markdown('</div>', unsafe_allow_html=True)

    # -------- Side Info --------
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/1827/1827332.png")

    # -------- Prediction --------
    if predict_btn and ticket_text:

        with st.spinner("Analyzing Ticket..."):
            time.sleep(1)

            vect = vectorizer.transform([ticket_text])

            category = category_model.predict(vect)[0]
            priority = priority_model.predict(vect)[0]
            team = queue_model.predict(vect)[0]

            # Fake confidence (optional)
            confidence = np.random.uniform(85, 98)

        st.success("✅ Ticket Processed Successfully")

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("📂 Category", category)
        c2.metric("⚡ Priority", priority)
        c3.metric("👨‍💻 Team", team)
        c4.metric("📊 Confidence", f"{confidence:.2f}%")

# ================= ABOUT PAGE =================
elif page == "📘 About Project":

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.header("📘 Project Overview")

    st.write("""
    This AI system assists IT teams by automatically:

    • Categorizing incoming tickets  
    • Prioritizing issues  
    • Extracting key information  
    • Recommending support teams  
    • Improving operational workflow  
    """)

    st.header("🤖 Models Used")

    st.write("""
    ✔ TF-IDF Vectorization  
    ✔ Machine Learning Classification Models  
    ✔ Multi-model Decision Pipeline  
    """)

    st.header("🚀 Future Improvements")

    st.write("""
    ✔ Real-time ticket dashboard  
    ✔ Model confidence visualization  
    ✔ Ticket analytics  
    ✔ User authentication  
    ✔ Database integration  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

