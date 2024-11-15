import streamlit as st
import pickle
import pandas as pd

# Load the trained Logistic Regression model and LabelEncoder
with open("logistic_regression_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

with open("label_encoder.pkl", "rb") as file:
    loaded_label_encoder = pickle.load(file)

# Streamlit app title
st.title("Disease Category Prediction")

# Collect input data
st.header("Enter Patient Data")

age = st.number_input("Age", min_value=0, max_value=120, value=68)
albumin = st.number_input("Albumin Level", min_value=0.0, value=43.0)
alkaline_phosphatase = st.number_input("Alkaline Phosphatase", min_value=0.0, value=22.9)
alanine_aminotransferase = st.number_input("Alanine Aminotransferase", min_value=0.0, value=5.0)
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0.0, value=42.1)
bilirubin = st.number_input("Bilirubin", min_value=0.0, value=12.0)
cholinesterase = st.number_input("Cholinesterase", min_value=0.0, value=7.29)
cholesterol = st.number_input("Cholesterol", min_value=0.0, value=4.89)
creatinina = st.number_input("Creatinine", min_value=0.0, value=80.9)
gamma_glutamyl_transferase = st.number_input("Gamma Glutamyl Transferase", min_value=0.0, value=11.9)
protein = st.number_input("Protein", min_value=0.0, value=76.1)
sex_f = st.radio("Sex", ("Female", "Male")) == "Female"
sex_m = not sex_f  # True if male, False if female

# Prepare input data for prediction
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
    'sex_f': [float(sex_f)],
    'sex_m': [float(sex_m)]
})

# Prediction button
if st.button("Predict Category"):
    sample_prediction_encoded = loaded_model.predict(sample_data)
    sample_prediction = loaded_label_encoder.inverse_transform(sample_prediction_encoded)
    st.subheader(f"Predicted Category: {sample_prediction[0]}")
