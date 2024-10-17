import streamlit as st

# Function to convert temperature
def convert_temperature(temp, unit):
    """Convert temperature between Celsius and Fahrenheit."""
    if unit == "Celsius to Fahrenheit":
        return (temp * 9/5) + 32
    elif unit == "Fahrenheit to Celsius":
        return (temp - 32) * 5/9

# Streamlit app interface
st.title("Temperature Converter")

# Select conversion type
conversion_type = st.selectbox(
    "Choose conversion type:",
    ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
)

# Input temperature
temp_input = st.slider("Select the temperature:", min_value=-100.0, max_value=100.0, step=0.1)

# Real-time conversion and display of result
converted_temp = convert_temperature(temp_input, conversion_type)
if conversion_type == "Celsius to Fahrenheit":
    st.write(f"{temp_input}°C is equal to {converted_temp:.2f}°F")
else:
    st.write(f"{temp_input}°F is equal to {converted_temp:.2f}°C")
