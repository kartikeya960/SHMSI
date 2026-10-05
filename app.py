import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Chloride Sensor Analysis", page_icon="🧪", layout="wide"
)

# App Title and Header
st.title("🧪 Low-Cost Quantitative Chloride Sensor")
st.markdown(
    "**ISEF Project:** Digital quantification of chloride via solid-phase matrix"
    " and $L^*a^*b^*$ computer vision."
)

# Sidebar for navigation
st.sidebar.header("Navigation")
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
      "Choose a sensor image...", type=["jpg", "jpeg", "png"]
  )

  if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Sensor Strip", use_column_width=True)

    # Placeholder for your OpenCV / L*a*b* analysis code
    st.info("Processing image and calculating L*a*b* values...")

    # Example output simulation (Replace this with your actual prediction logic later!)
    st.success("Estimated Chloride Concentration: **-- mg/L**")

elif app_mode == "Dataset (112 Runs)":
  st.header("Experimental Dataset Overview")
  st.write(
      "Here is the summary of your 112 experimental runs used for calibration"
      " and validation."
  )

  # You can load your dataset here later using pandas!
  # df = pd.read_excel("Results table.xlsx")
  # st.dataframe(df)

  st.metric(label="Total Completed Runs", value="112")
  st.metric(label="Estimated Cost Per Sensor", value="~€0.47")
