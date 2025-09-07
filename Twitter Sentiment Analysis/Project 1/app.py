import streamlit as st
import pickle
import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ==============================
# Load Model and Vectorizer
# ==============================
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ==============================
# Preprocessing Function
# ==============================
ps = PorterStemmer()

def transform_text(text):
    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove mentions and hashtags
    text = re.sub(r"@\w+|#", "", text)

    # Tokenization
    tokens = nltk.word_tokenize(text)

    # Remove stopwords & punctuation, keep only alphanumeric
    cleaned_tokens = []
    for word in tokens:
        if word.isalnum() and word not in stopwords.words("english") and word not in string.punctuation:
            cleaned_tokens.append(ps.stem(word))

    return " ".join(cleaned_tokens)

# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="Twitter Sentiment Analysis", page_icon="🐦", layout="centered")

st.title("🐦 Twitter Sentiment Analysis")
st.write("Enter a tweet below and let the model predict whether it's **Positive**, **Neutral**, or **Negative**.")

# Input box
user_input = st.text_area("✍️ Type your tweet here:")

# Predict button
if st.button("🔮 Predict Sentiment"):
    if user_input.strip() != "":
        # Preprocess
        transformed_text = transform_text(user_input)

        # Vectorize
        vectorized = vectorizer.transform([transformed_text]).toarray()

        # Predict
        prediction = model.predict(vectorized)[0]

        sentiment_map = {0: "Negative 😡", 1: "Neutral 😐", 2: "Positive 😍"}
        st.subheader("Result:")
        st.success(sentiment_map[prediction])
    else:
        st.warning("⚠️ Please enter a tweet before predicting.")
