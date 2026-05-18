import streamlit as st
import gspread
from google.auth import default
from datetime import datetime

# 1. Page Configuration Setup
st.set_page_config(page_title="Agro-Data Platform", page_icon="🌾", layout="centered")

st.title("🌾 Agro-Data Trading & Logistics Platform")
st.markdown("Enter transaction details below to update the cloud database instantly.")

# 2. Database Connection Engine
@st.cache_resource
def connect_to_sheets():
    try:
        gc = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
        spreadsheet = gc.open("Agro_Market_Database")
        return spreadsheet.sheet1
    except Exception as e:
        return None
      sheet = connect_to_sheets()

# 3. User Interface Forms
st.header("👤 Farmer & Product Details")
farmer_name = st.text_input("Farmer Full Name")
phone_num   = st.text_input("Phone Number")
address     = st.text_input("Full Address (Region/Zone/Woreda)")

col1, col2 = st.columns(2)
with col1:
    product_name  = st.selectbox("Product Type", ["Teff", "Wheat", "Coffee", "Barley", "Maize"])
with col2:
    product_grade = st.selectbox("Product Grade", ["Grade 1", "Grade 2", "Grade 3"])

st.header("💰 Financial & Logistics Metrics")
col3, col4, col5 = st.columns(3)
with col3:
    quantity = st.number_input("Quantity (Quintals)", min_value=1, step=1)
with col4:
    price_per_q = st.number_input("Purchase Price / Q (ETB)", min_value=0.0)
with col5:
    selling_per_q = st.number_input("Selling Price / Q (ETB)", min_value=0.0)

col6, col7 = st.columns(2)
with col6:
    transport_per_q = st.number_input("Transport / Q (ETB)", min_value=0.0)
with col7:
    loading_per_q = st.number_input("Loading Fee / Q (ETB)", min_value=0.0)
