import streamlit as st
import joblib

# Load Models
category_model = joblib.load("category_model.pkl")
priority_model = joblib.load("priority_model.pkl")
queue_model = joblib.load("queue_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

priority_map = {
    1: "Low",
    2: "Medium",
    3: "High"
}

# Prediction Function
def predict_ticket(ticket_text):

    text_vector = tfidf.transform([ticket_text])

    category = category_model.predict(text_vector)[0]
    priority = int(priority_model.predict(text_vector)[0])
    queue = queue_model.predict(text_vector)[0]

    return category, priority_map.get(priority, priority), queue


# Streamlit UI
st.title("AI IT Ticket Assistant")

ticket_text = st.text_area("Enter Ticket Description")

if st.button("Predict"):

    if ticket_text.strip() == "":
        st.warning("Please enter ticket description")
    else:
        category, priority, queue = predict_ticket(ticket_text)

        st.success("Prediction Result")

        st.write("Category:", category)
        st.write("Priority:", priority)
        st.write("Recommended Team:", queue)
