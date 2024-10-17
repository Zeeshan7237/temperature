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

# Input temperature with both slider and manual entry
st.write("You can either use the slider or type in the value below:")

# Slider for interactive input
temp_slider = st.slider("Select the temperature using the slider:", min_value=-100.0, max_value=100.0, step=0.1)

# Text input for manual temperature entry
temp_input = st.number_input("Or type the temperature:", value=temp_slider, step=0.1)

# Sync slider with manual input
temp_input = st.slider("Adjust temperature manually:", min_value=-100.0, max_value=100.
