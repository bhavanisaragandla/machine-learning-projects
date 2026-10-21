import streamlit as st
import joblib
import pandas as pd

# Load the trained model

@st.cache_resource
def load_model():
return joblib.load("model.pkl")

model = load_model()

st.title("✈️ Flight Price Prediction")
st.write("Enter your flight details to predict the ticket price.")

# IMPORTANT:

# Replace these sample inputs with the exact features

# and preprocessing used by your trained model.

st.info(
"The prediction interface must match the features "
"used when training your model."
)

st.write("Model loaded successfully!")
