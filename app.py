import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import datetime
from datetime import datetime as dt
import time
import base64
import pickle 
from xgboost import XGBClassifier

# Title
st.title("UPI Transaction Fraud Detector")

# Load the saved XGBoost model from the pickle file
pickle_file_path = "UPI Fraud Detection Final.pkl"
loaded_model = pickle.load(open(pickle_file_path, 'rb'))

# Dropdown values
tt = ["Bill Payment", "Investment", "Other", "Purchase", "Refund", "Subscription"]
pg = ["Google Pay", "HDFC", "ICICI UPI", "IDFC UPI", "Other", "Paytm", "PhonePe", "Razor Pay"]
ts = ['Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand',
      'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
      'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
mc = ['Donations and Devotion', 'Financial services and Taxes', 'Home delivery', 'Investment', 'More Services', 'Other',
      'Purchases', 'Travel bookings', 'Utilities']

# Single Transaction Input
tran_date = st.date_input("Select the date of your transaction", datetime.date.today())
if tran_date:
    selected_date = dt.combine(tran_date, dt.min.time())
    month = selected_date.month
    year = selected_date.year

tran_type = st.selectbox("Select transaction type", tt)
pmt_gateway = st.selectbox("Select payment gateway", pg)
tran_state = st.selectbox("Select transaction state", ts)
merch_cat = st.selectbox("Select merchant category", mc)
amt = st.number_input("Enter transaction amount", step=0.1)

# Submit Button
button_clicked = st.button("Check transaction")

# Styling the button
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

if button_clicked:
    with st.spinner("Checking transaction..."):
        # One-hot encodings
        tt_oh = [0] * len(tt)
        pg_oh = [0] * len(pg)
        ts_oh = [0] * len(ts)
        mc_oh = [0] * len(mc)

        tt_oh[tt.index(tran_type)] = 1
        pg_oh[pg.index(pmt_gateway)] = 1
        ts_oh[ts.index(tran_state)] = 1
        mc_oh[mc.index(merch_cat)] = 1

        # Input vector
        input = [amt, year, month] + tt_oh + pg_oh + ts_oh + mc_oh
        result = loaded_model.predict([input])[0]

        st.success("Transaction Checked!")
        if result == 0:
            st.write("✅ This transaction is **not fraudulent**.")
        else:
            st.write("🚨 This transaction is **fraudulent**.")
