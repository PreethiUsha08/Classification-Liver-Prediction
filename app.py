
import streamlit as st
import pickle
import pandas as pd

# Load the saved Logistic Regression model
with open("logistic_regression_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Define category mapping for interpretability
category_mapping = {0: 'cirrhosis', 1: 'fibrosis', 2: 'hepatitis', 3: 'no_disease', 4: 'suspect_disease'}

# Streamlit app title
st.title("Disease Category Prediction App")

# Input fields for each feature
st.sidebar.header("Input Patient Data")

age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=68)
albumin = st.sidebar.number_input("Albumin", min_value=0.0, max_value=100.0, value=43.0)
alkaline_phosphatase = st.sidebar.number_input("Alkaline Phosphatase", min_value=0.0, max_value=500.0, value=22.9)
alanine_aminotransferase = st.sidebar.number_input("Alanine Aminotransferase", min_value=0.0, max_value=500.0, value=5.0)
aspartate_aminotransferase = st.sidebar.number_input("Aspartate Aminotransferase", min_value=0.0, max_value=500.0, value=42.1)
bilirubin = st.sidebar.number_input("Bilirubin", min_value=0.0, max_value=100.0, value=12.0)
cholinesterase = st.sidebar.number_input("Cholinesterase", min_value=0.0, max_value=100.0, value=7.29)
cholesterol = st.sidebar.number_input("Cholesterol", min_value=0.0, max_value=100.0, value=4.89)
creatinina = st.sidebar.number_input("Creatinina", min_value=0.0, max_value=500.0, value=80.9)
gamma_glutamyl_transferase = st.sidebar.number_input("Gamma-Glutamyl Transferase", min_value=0.0, max_value=500.0, value=11.9)
protein = st.sidebar.number_input("Protein", min_value=0.0, max_value=100.0, value=76.1)
sex_f = st.sidebar.selectbox("Sex: Female", [0, 1])
sex_m = st.sidebar.selectbox("Sex: Male", [0, 1])

# Collect input data into a DataFrame
sample_data = pd.DataFrame({
    'age': [age],
    'albumin': [albumin],
    'alkaline_phosphatase': [alkaline_phosphatase],
    'alanine_aminotransferase': [alanine_aminotransferase],
    'aspartate_aminotransferase': [aspartate_aminotransferase],
    'bilirubin': [bilirubin],
    'cholinesterase': [cholinesterase],
    'cholesterol': [cholesterol],
    'creatinina': [creatinina],
    'gamma_glutamyl_transferase': [gamma_glutamyl_transferase],
    'protein': [protein],
    'sex_f': [sex_f],
    'sex_m': [sex_m]
})

# Predict and display results
if st.button("Predict Disease Category"):
    prediction = loaded_model.predict(sample_data)
    predicted_category = category_mapping[prediction[0]]
    st.write(f"Prediction for the sample data: **{predicted_category}**")
