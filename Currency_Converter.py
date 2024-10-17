import streamlit as st
import requests

# Function to get exchange rates
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency, None)

# Streamlit UI
def main():
    # Title and description
    st.title("🌍💸 Currency Converter")
    st.markdown("""
        <style>
        .reportview-container {
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
            color: #fff;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: #fff;
        }
        .stTextInput>div>input {
            background-color: #e3e3e3;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.subheader("Convert from one currency to another with real-time exchange rates!")

    # Currency selection
    base_currency = st.selectbox("Choose your base currency", ['USD', 'EUR', 'GBP', 'INR', 'JPY', 'AUD'])
    target_currency = st.selectbox("Choose your target currency", ['USD', 'EUR', 'GBP', 'INR', 'JPY', 'AUD'])

    # Input amount
    amount = st.number_input("Enter the amount", min_value=0.0, value=1.0, step=0.01)

    # Convert button
    if st.button("Convert"):
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        if exchange_rate:
            converted_amount = round(amount * exchange_rate, 2)
            st.success(f"{amount} {base_currency} = {converted_amount} {target_currency}")
        else:
            st.error(f"Unable to retrieve exchange rate for {base_currency} to {target_currency}")

if __name__ == "__main__":
    main()
