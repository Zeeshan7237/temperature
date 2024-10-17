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
temp_input = st.number_input("Enter the temperature:", step=0.1)

# Convert and display result when the user clicks the button
if st.button("Convert"):
    converted_temp = convert_temperature(temp_input, conversion_type)
    if conversion_type == "Celsius to Fahrenheit":
        st.write(f"{temp_input}°C is equal to {converted_temp:.2f}°F")
    else:
        st.write(f"{temp_input}°F is equal to {converted_temp:.2f}°C")

# Option to continue or exit
st.write("Do you want to perform another conversion?")
if st.button("Yes"):
    st.experimental_rerun()  # Restarts the app for a new conversion
elif st.button("No"):
    st.write("Thank you for using the Temperature Converter!")
