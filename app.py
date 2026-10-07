import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Chloride Sensor Analysis", layout="wide"
)

# App Title and Header
st.title("S.H.M.S.I (smart health onitoring system interface)")
st.markdown(
    "**FJSL Project in Miersch, Luxembourg:** Digital quantification of chloride via solid-phase matrix"
    " and $L^*a^*b^*$ computer vision.(!TEST SUBJECT!)"
)

# Sidebar navi
st.sidebar.header("Navigate")
app_mode = st.sidebar.selectbox(
    "Choose a section:", ["Sensor Analysis (Live Upload)", "Dataset (112 Runs)"]
)

if app_mode == "Sensor Analysis (Live Upload)":
  st.header("Image Processing Pipeline")
  st.write(
      "Upload a photograph of your tested sensor strip to extract colorimetry"
      " values and estimate chloride concentration."
  )

  uploaded_file = st.file_uploader(
      "Choose a sensor image Here", type=["jpg, jpeg, png"]
  )

  if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Sensor's colourmetric response strip here", use_column_width=True)

    # L*A*B FUNCTION
    st.info("Processing image and calculating L*a*b* values...")or("Buffering....")

    # Example output simulation
    st.success("Estimated Chloride Concentration: **-- mg/L**")

elif app_mode == "Dataset (112 Runs)":
  st.header("Experimental Dataset Overview")
  st.write(
      "Here is the summary of your 112 experimental runs used for calibration"
      " and validation."
  )

  st.metric(label="Total Completed Runs(Hardware)", value="112")
  st.metric(label="Estimated Cost Per Sensor", value="~€0.47")
  st.metric(label="Total porposal of runs(Software)", value="160")
  st.metric(label="Total amount oof equations used in this software", value="3")