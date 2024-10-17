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

# Input temperature using both slider and manual entry
st.write("You can either use the slider or manually type in the value:")

# Slider for interactive input
temp_slider = st.slider("Select the temperature using the slider:", min_value=-100.0, max_value=100.0, step=0.1)

# Text input for manual temperature entry (linked to the slider)
temp_input = st.number_input("Or type the temperature:", value=temp_slider, step=0.1)

# Ensure synchronization between the slider and number input
if temp_input != temp_slider:
    temp_slider = temp_input

# Real-time conversion and display of result
converted_temp = convert_temperature(temp_slider, conversion_type)
if conversion_type == "Celsius to Fahrenheit":
    st.write(f"{temp_slider}°C is equal to {converted_temp:.2f}°F")
else:
    st.write(f"{temp_slider}°F is equal to {converted_temp:.2f}°C")
