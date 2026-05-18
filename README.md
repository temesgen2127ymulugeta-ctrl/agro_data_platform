import csv
from datetime import datetime
from google.colab import files

# 1. Database initialization
agro_market_data = []

print("=========================================================")
print("---    AGRO-DATA TRADING INTEL PLATFORM v4.0 (ENG)    ---")
print("=========================================================")

while True:
    print("\n--- Enter Record Details ---")
    
    # A. Logistics and Demographics Entry
    farmer_name = input("Enter Farmer Full Name: ")
    phone_num   = input("Enter Phone Number: ")
    address     = input("Enter Full Address (Region/Zone/Woreda): ")
    
    # B. Crop Specs
    product_name  = input("Enter Product Type (e.g., Teff, Wheat, Coffee): ")
    product_grade = input("Enter Product Grade (e.g., Grade 1, Grade 2): ")
    
    # C. Financial & Volumetric Metrics
    quantity    = int(input("Enter Quantity in Quintals: "))
    price_per_q = float(input("Enter Purchase Price per Quintal (ETB): "))
    selling_per_q = float(input("Enter Estimated Selling Price per Quintal (ETB): "))
    
    # D. Friction Costs (Logistics)
    transport_per_q = float(input("Enter Transport Cost per Quintal (ETB): "))
    loading_per_q   = float(input("Enter Loading/Unloading Cost per Quintal (ETB): "))
    
    # E. Advanced Financial Engine (Automatic Calculations)
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_purchase_value = quantity * price_per_q
    total_transport     = quantity * transport_per_q
    total_loading       = quantity * loading_per_q
    grand_total_cost    = total_purchase_value + total_transport + total_loading
    
    total_revenue       = quantity * selling_per_q
    net_profit          = total_revenue - grand_total_cost
    profit_margin_pct   = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0
    
    # 2. Package data inside an organized dictionary structure
    product_entry = {
        "timestamp": current_timestamp,
        "farmer": farmer_name,
        "phone": phone_num,
        "address": address,
        "product": product_name,
        "grade": product_grade,
        "quantity": quantity,
        "purchase_price": price_per_q,
        "selling_price": selling_per_q,
        "total_product_cost": total_purchase_value,
        "total_transport": total_transport,
        "total_loading": total_loading,
        "grand_total_cost": grand_total_cost,
        "total_revenue": total_revenue,
        "net_profit": net_profit,
        "margin_pct": round(profit_margin_pct, 2)
    }
    
    # 3. Commit to database list
    agro_market_data.append(product_entry)
    print("\nRecord Successfully Saved and Verified!")
    
    # 4. Control Check for loop continuation
    repeat = input("\nDo you want to register another farmer? (yes/no): ").strip().lower()
    if repeat != "yes":
        break
