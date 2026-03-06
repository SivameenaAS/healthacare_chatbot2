import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# -------------------------------
# Load datasets
# -------------------------------

training = pd.read_csv(r"C:\Users\aathi\OneDrive\Documents\healthcare_chatbot\training.csv")
severity = pd.read_csv(r"C:\Users\aathi\OneDrive\Documents\healthcare_chatbot\Symptom-severity (2).csv")
description = pd.read_csv(r"C:\Users\aathi\OneDrive\Documents\healthcare_chatbot\symptom_Description.csv")
precaution = pd.read_csv(r"C:\Users\aathi\OneDrive\Documents\healthcare_chatbot\symptom_precaution.csv")

# -------------------------------
# Prepare Data
# -------------------------------

X = training.drop("prognosis", axis=1)
y = training["prognosis"]

model = DecisionTreeClassifier()
model.fit(X, y)

symptoms_list = X.columns.tolist()

# -------------------------------
# Prediction Function
# -------------------------------

def predict_disease(symptoms):

    input_data = [0] * len(symptoms_list)

    for symptom in symptoms:
        if symptom in symptoms_list:
            index = symptoms_list.index(symptom)
            input_data[index] = 1

    prediction = model.predict([input_data])

    return prediction[0]

# -------------------------------
# Get Description
# -------------------------------

def get_description(disease):

    desc = description[description['Disease'] == disease]['Description']

    if not desc.empty:
        return desc.values[0]
    else:
        return "Description not available"

# -------------------------------
# Get Precautions
# -------------------------------

def get_precautions(disease):

    row = precaution[precaution['Disease'] == disease]

    if not row.empty:
        return row.values[0][1:]
    else:
        return ["No precaution available"]

# -------------------------------
# Streamlit UI
# -------------------------------

st.title("🩺 Healthcare Chatbot")

st.write("Select your symptoms and get possible disease prediction")

selected_symptoms = st.multiselect(
    "Select Symptoms",
    symptoms_list
)

if st.button("Predict Disease"):

    if len(selected_symptoms) == 0:
        st.warning("Please select symptoms")

    else:

        disease = predict_disease(selected_symptoms)

        st.success(f"Predicted Disease: {disease}")

        desc = get_description(disease)
        st.subheader("Disease Description")
        st.write(desc)

        st.subheader("Precautions")

        precautions = get_precautions(disease)

        for p in precautions:
            st.write("✔", p)