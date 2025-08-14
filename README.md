# UPI-fraud
A upi fraud detction model
UPI Fraud Detection

A machine learning-based solution for detecting fraudulent UPI transactions in real time. The system uses trained models to classify transactions as Fraud or Not Fraud, helping enhance digital payment security.

🚀 Features

Detects suspicious UPI transactions with high accuracy

Pre-trained model ready for deployment

Flask API for real-time prediction

Example dataset and notebook for retraining

Easy to integrate into payment systems

🛠 Tech Stack

Python – Core development

Pandas & NumPy – Data processing

Scikit-learn – Machine learning model

Flask – API endpoint for prediction

Jupyter Notebook – Model training & evaluation

📂 Repository Structure
UPI-fraud/
│── UPI_fraud_detection_capstone_project.ipynb   # Model building & training
│── UPI Fraud Detection Final.pkl                # Saved ML model
│── app.py                                       # Flask API script
│── requirements.txt                             # Python dependencies
│── sample.csv                                   # Sample input data

⚙️ Installation & Usage

1. Clone the repo

git clone https://github.com/Deepanshubhargav1/UPI-fraud.git
cd UPI-fraud


2. Install dependencies

pip install -r requirements.txt


3. Run the Flask API

python app.py


Access the API at: http://127.0.0.1:5000/predict

4. Test with sample data
Use sample.csv or send JSON data matching the model’s expected features.

📊 How It Works

Transaction data is preprocessed (missing values handled, features encoded).

Machine learning model (e.g., Random Forest) predicts fraud likelihood.

Flask API returns Fraud or Not Fraud label.
