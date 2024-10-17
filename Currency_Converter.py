import streamlit as st
import requests

# Dictionary mapping countries to currency codes
country_currency_map = {
    'United States': 'USD', 'Eurozone': 'EUR', 'United Kingdom': 'GBP', 'India': 'INR', 
    'Pakistan': 'PKR', 'Bangladesh': 'BDT', 'Japan': 'JPY', 'Australia': 'AUD', 'Canada': 'CAD', 
    'China': 'CNY', 'Singapore': 'SGD', 'Malaysia': 'MYR', 'Thailand': 'THB', 
    'South Africa': 'ZAR', 'United Arab Emirates': 'AED', 'Switzerland': 'CHF', 
    'Saudi Arabia': 'SAR', 'New Zealand': 'NZD', 'Indonesia': 'IDR', 'South Korea': 'KRW'
}

# Function to get exchange rates
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency, None)

# Function to convert country name to currency code
def get_currency_code(input_str):
    input_str = input_str.strip().title()  # Format input
    if input_str in country_currency_map:
        return country_currency_map[input_str]  # Return currency code if it's a country name
    elif input_str in country_currency_map.values():
        return input_str  # Return the currency code itself
    else:
        return None  # Invalid input

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
        .stTextInput>div>input {
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
        .css-1dp5vir {
            font-size: 20px;
            color: #4B0082;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("💸 Real-Time Currency Converter")
    st.subheader("✨ Convert Currencies with Style & Real-Time Exchange Rates!")

    # Autocomplete for base currency input
    base_input = st.text_input("🌍 Enter the base currency code or country name", "United States")
    # Autocomplete for target currency input
    target_input = st.text_input("💱 Enter the target currency code or country name", "India")

    # Input amount
    amount = st.number_input("💰 Enter the amount", min_value=0.0, value=1.0, step=0.01)

    # Convert button
    if st.button("Convert Now 🚀"):
        # Convert country names to currency codes
        base_currency = get_currency_code(base_input)
        target_currency = get_currency_code(target_input)

        if base_currency and target_currency:
            exchange_rate = get_exchange_rate(base_currency, target_currency)
            if exchange_rate:
                converted_amount = round(amount * exchange_rate, 2)
                st.success(f"🎉 {amount} {base_input} ({base_currency}) = {converted_amount} {target_input} ({target_currency})")
            else:
                st.error(f"⚠️ Unable to retrieve exchange rate for {base_currency} to {target_currency}")
        else:
            st.error("❌ Invalid country name or currency code. Please check your inputs.")

    # Suggestions for autocomplete
    suggestions = list(country_currency_map.keys()) + list(country_currency_map.values())
    st.markdown(f"**Suggestions:** {', '.join(suggestions)}")

if __name__ == "__main__":
    main()
