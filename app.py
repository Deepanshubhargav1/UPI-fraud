import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import datetime
from datetime import datetime as dt
import time
import base64
import pickle 
# import subprocess
# subprocess.check_call(["pip", "install", "xgboost"])
from xgboost import XGBClassifier

"""
# Welcome to your own UPI Transaction Fraud Detector!

You have the option of inspecting a single transaction by adjusting the parameters below OR you can even check 
multiple transactions at once by uploading a .csv file in the specified format
"""

pickle_file_path = "UPI Fraud Detection Final.pkl"
# Load the saved XGBoost model from the pickle file
loaded_model = pickle.load(open(pickle_file_path, 'rb'))

tt = ["Bill Payment", "Investment", "Other", "Purchase", "Refund", "Subscription"]
pg = ["Google Pay", "HDFC", "ICICI UPI", "IDFC UPI", "Other", "Paytm", "PhonePe", "Razor Pay"]
ts = ['Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
mc = ['Donations and Devotion', 'Financial services and Taxes', 'Home delivery', 'Investment', 'More Services', 'Other', 'Purchases', 'Travel bookings', 'Utilities']

tran_date = st.date_input("Select the date of your transaction", datetime.date.today())
if tran_date:
    selected_date = dt.combine(tran_date, dt.min.time())
    month = selected_date.month
    year = selected_date.year

tran_type = st.selectbox("Select transaction type", tt)
pmt_gateway = st.selectbox("Select payment gateway", pg)
tran_state=st.selectbox("Select transaction state",ts)
merch_cat = st.selectbox("Select merchant category", mc)

amt = st.number_input("Enter transaction amount",step=0.1)


button_clicked = st.button("Check transaction(s)")
st.markdown(
    """
    <style>
    .stButton>button {
        position: fixed;
        bottom: 40px;
        left: 413px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
results = []
if button_clicked:
    tt_oh = []
    for i in range(len(tt)):
        tt_oh.append(0)
    pg_oh = []
    for i in range(len(pg)):
        pg_oh.append(0)
    ts_oh = []
    for i in range(len(ts)):
        ts_oh.append(0)
    mc_oh = []
    for i in range(len(mc)):
        mc_oh.append(0)
else:
     with st.spinner("Checking transaction(s)..."):
            result = loaded_model.predict(inputs)[0]
            st.success("Checked transaction!")
            if(result==0):
                st.write("Congratulations! Not a fraudulent transaction.")
            else:
                st.write("Oh no! This transaction is fraudulent.")
