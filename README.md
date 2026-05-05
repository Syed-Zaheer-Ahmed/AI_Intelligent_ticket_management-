# 🤖 AI IT Ticket Assistant (Streamlit)

An end‑to‑end Machine Learning project that automatically predicts **IT support team** and **ticket priority** from user queries using NLP and a Streamlit web app.

---

## 📌 Project Overview

IT support teams receive hundreds of tickets daily. Manually assigning them to the correct team and priority is slow and error‑prone.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to:

* Classify incoming IT tickets into the correct **support team**
* Predict the **priority level** of the ticket
* Provide a simple **Streamlit UI** for real‑time predictions

---

## 🎯 Features

* Text preprocessing & cleaning pipeline
* NLP vectorization using **TF‑IDF**
* Two ML models:

  * Team Classification Model
  * Priority Classification Model
* Real‑time predictions via Streamlit
* Clean, beginner‑friendly project structure

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Preprocessing

* Removed null values
* Lowercasing text
* Removed special characters
* Removed team keywords to prevent data leakage
* Train/test split

### 2️⃣ Text Vectorization

Used **TF‑IDF Vectorizer** to convert ticket text into numerical features.

### 3️⃣ Model Training

Two separate models were trained:

| Model          | Purpose                     |
| -------------- | --------------------------- |
| Team Model     | Predict responsible IT team |
| Priority Model | Predict ticket urgency      |

Algorithms used:

* Logistic Regression / Naive Bayes (depending on training notebook)

### 4️⃣ Model Saving

Models were saved using **pickle/joblib**:

```
models/
├── category_model.joblib
├── priority_model.joblib
├── queue_model.joblib
├── tfidf_vectorizer.joblibl
```

---

## 🖥️ Streamlit App

The Streamlit app allows users to enter a ticket and instantly receive predictions.

### App Capabilities

* User enters IT issue description
* App cleans text automatically
* Predicts:

  * Assigned Team
  * Priority Level
* Displays results instantly

---

## 📂 Project Structure

```

AI-IT-Ticket-Assistant/
│
├── README.md
├── Notebook.ipynb
├── app.py
├── requirements.txt
│
├── category_model.joblib
├── priority_model.joblib
├── queue_model.joblib
├── tfidf_vectorizer.joblib

```



---

## 🧾 Example Input

**Input Ticket:**

```
Users cannot connect to VPN from remote locations.
```

**Output:**

```
Team: Technical Support
Priority: 2
```

---

## 🛠️ Requirements

Example `requirements.txt`:

```
streamlit
scikit-learn
pandas
numpy
joblib
```

---

## 🚀 Future Improvements

* Add ticket category prediction
* Deploy app on Streamlit Cloud
* Add model retraining pipeline
* Add dashboard analytics
* Integrate with real ticketing systems (Jira, ServiceNow)

# 🧪 Example Queries to Try

Paste these into the app:

* VPN disconnects every 15 minutes
* Laptop screen flickering after update
* Unable to access company email
* Firewall blocking external access
* Virtual machine not starting
* Password reset required repeatedly

---

# 🎯 Real-World Use Case

This system replicates automation used in:

* ServiceNow
* Jira Service Desk
* Zendesk
* Freshdesk

It helps companies:

* Reduce ticket triage time
* Improve response speed
* Automate ticket routing

---

# 🛠️ Tech Stack

* Python
* Scikit-learn
* NLP (TF-IDF)
* Streamlit
* Joblib

---

## 👨‍💻 Author

**Syed Zaheer**

---

## Streamlit Deployment Link
https://cdq6gjyqtepimt2lefixd8.streamlit.app/

---

