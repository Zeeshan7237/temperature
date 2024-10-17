import streamlit as st
import requests

# Dictionary mapping countries to currency codes
country_currency_map = {
    'United States': 'USD', 'Eurozone': 'EUR', 'United Kingdom': 'GBP', 'India': 'INR', 
    'Pakistan': 'PKR', 'Bangladesh': 'BDT', 'Japan': 'JPY', 'Australia': 'AUD', 
    'Canada': 'CAD', 'China': 'CNY', 'Singapore': 'SGD', 'Malaysia': 'MYR', 
    'Thailand': 'THB', 'South Africa': 'ZAR', 'United Arab Emirates': 'AED', 
    'Switzerland': 'CHF', 'Saudi Arabia': 'SAR', 'New Zealand': 'NZD', 
    'Indonesia': 'IDR', 'South Korea': 'KRW'
}

# Function to get exchange rates
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency, None)

# Streamlit UI
def main():
    # Title and description
    st.markdown("""
        <style>
        .reportview-container {
            background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
            color: #000;
        }
        h1, h2, h3, h4 {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            color: #FF4500;
            text-align: center;
        }
        .stButton>button {
            background: linear-gradient(135deg, #FC466B 0%, #3F5EFB 100%);
            color: white;
            border-radius: 10px;
            font-size: 18px;
        }
        .stSelectbox>div>select {
            background-color: #e3e3e3;
            color: black;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
        .stNumberInput>div>input {
            background-color: #e3e3e3;
            color: black;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("💸 Real-Time Currency Converter")
    st.subheader("✨ Convert Currencies with Style & Real-Time Exchange Rates!")

    # Dropdown for selecting the base country
    base_country = st.selectbox("🌍 Select the base country", list(country_currency_map.keys()))
    # Dropdown for selecting the target country
    target_country = st.selectbox("💱 Select the target country", list(country_currency_map.keys()))

    # Input amount
    amount = st.number_input("💰 Enter the amount", min_value=0.0, value=1.0, step=0.01)

    # Convert button
    if st.button("Convert Now 🚀"):
        base_currency = country_currency_map[base_country]
        target_currency = country_currency_map[target_country]
        
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        if exchange_rate:
            converted_amount = round(amount * exchange_rate, 2)
            st.success(f"🎉 {amount} {base_country} ({base_currency}) = {converted_amount} {target_country} ({target_currency})")
        else:
            st.error(f"⚠️ Unable to retrieve exchange rate for {base_country} to {target_country}")

if __name__ == "__main__":
    main()
