import numpy as np
import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Colorimetric pH Sensor Analysis",
    page_icon="🧪",
    layout="centered",
)

st.title("🧪 Colorimetric pH Sensor Analysis Tool")
st.markdown(
    "Analyzing biosensor calibration, sigmoidal fits, and Henderson-Hasselbalch validation."
)

# Sidebar controls for simulation/input
st.sidebar.header("Calibration Parameters")
pka_input = st.sidebar.slider("Estimated pKa", 5.0, 7.0, 5.83, 0.01)

# Generate sample synthetic calibration data if none is uploaded
st.subheader("1. Sigmoidal Henderson-Hasselbalch Response Curve")

# Simulated pH range around the target biomedical window
ph_vals = np.linspace(4.0, 8.0, 100)


# Sigmoidal response model (Hill-type / Henderson-Hasselbalch form)
def sigmoidal_response(pH, pka):
    # Normalized response from 0 to 1 based on pKa
    return 1 / (1 + 10 ** (pka - pH))


response_vals = sigmoidal_response(ph_vals, pka_input)

# Display data table
chart_data = pd.DataFrame(
    {"pH": ph_vals, "Calculated Normalized Absorbance/RGB": response_vals}
)

st.line_chart(chart_data, x="pH")

st.success(
    f"Model successfully loaded! Current established $pK_a$: **{pka_input}**"
)

# Quick Calculator Section
st.subheader("2. Quick pH Predictor from Sensor Reading")
user_reading = st.slider(
    "Sensor Normalized RGB/Intensity Value", 0.0, 1.0, 0.5, 0.01
)

if user_reading > 0 and user_reading < 1:
    # Inverse Henderson-Hasselbalch calculation
    calculated_pH = pka_input - np.log10((1 / user_reading) - 1)
    st.metric(label="Predicted pH", value=round(calculated_pH, 2))
else:
    st.info("Adjust the sensor reading slider to calculate corresponding pH.")