import streamlit as st
import pickle
import pandas as pd
from serial_reader import read_serial_data
from utils.preprocessing import preprocess_input

# Load trained model
with open('models/stress_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Real-Time Stress Detection", layout="wide")
st.title("🧠 Real-Time Stress Detection System")
st.markdown("Detect stress level using biosensor data streamed via ESP32.")

if st.button("Start Live Detection"):
    data = read_serial_data()
    if data:
        df = pd.DataFrame([data])
        processed = preprocess_input(df)
        prediction = model.predict(processed)
        st.success(f"Predicted Stress Level: **{prediction[0]}**")
    else:
        st.warning("No data received from sensor.")
