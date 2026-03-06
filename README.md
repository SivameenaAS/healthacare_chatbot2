# healthacare_chatbot2
This project is built using Python, Machine Learning, and Streamlit to create an interactive web interface where users can easily input symptoms and receive predictions instantly.
Data Collection
The project uses healthcare datasets containing symptoms and diseases.
training.csv – symptoms and disease labels
Symptom-severity.csv – severity level of symptoms
symptom_Description.csv – disease descriptions
symptom_precaution.csv – precautions for diseasesData Loading
The datasets are loaded using Pandas for further processing.

Data Preparation
Symptoms are used as input features (X)
Disease names are used as the target variable (y)

Model Training
A Decision Tree Classifier from Scikit-learn is trained to learn the relationship between symptoms and diseases.

User Input
The user selects symptoms through the Streamlit web interface.

Disease Prediction
The trained model analyzes the selected symptoms and predicts the most likely disease.

Result Display
The application displays:

Predicted disease

Disease description

Recommended precautions
