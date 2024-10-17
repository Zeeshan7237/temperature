import streamlit as st

# Function to convert temperature
def convert_temperature(temp, unit):
    """Convert temperature between Celsius and Fahrenheit."""
    if unit == "Celsius to Fahrenheit":
        return (temp * 9/5) + 32
    elif unit == "Fahrenheit to Celsius":
        return (temp - 32) * 5/9

# Streamlit app interface
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌡️ Temperature Converter 🌡️</h1>", unsafe_allow_html=True)
st.write("Convert between Celsius and Fahrenheit effortlessly with this simple tool.")

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Columns for layout
col1, col2 = st.columns(2)

# Conversion type selector
with col1:
    st.markdown("### Select Conversion Type:")
    conversion_type = st.selectbox(
        "",
        ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    )

# Temperature input with slider and manual entry
with col2:
    st.markdown("### Enter Temperature:")
    temp_slider = st.slider("Use the slider:", min_value=-100.0, max_value=100.0, step=0.1, value=0.0)
    temp_input = st.number_input("Or manually input the temperature:", value=temp_slider, step=0.1)

# Synchronize slider with number input
if temp_input != temp_slider:
    temp_slider = temp_input

# Real-time conversion and display result
converted_temp = convert_temperature(temp_slider, conversion_type)

# Adding a horizontal divider
st.markdown("<hr>", unsafe_allow_html=True)

# Display the result in an engaging way
if conversion_type == "Celsius to Fahrenheit":
    st.markdown(f"<h3 style='text-align: center; color: #FF5722;'>{temp_slider}°C is equal to {converted_temp:.2f}°F</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='text-align: center; color: #FF5722;'>{temp_slider}°F is equal to {converted_temp:.2f}°C</h3>", unsafe_allow_html=True)

# Add some footer text
st.markdown("<br><hr><p style='text-align: center;'>Created with ❤️ using Streamlit</p>", unsafe_allow_html=True)
