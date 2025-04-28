import streamlit as st

# Define available unit categories and conversion factors
unit_categories = {
    "Length": {
        "units": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "conversions": {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048,
            "Inches": 0.0254,
        },
    },
    "Weight": {
        "units": ["Kilograms", "Grams", "Pounds", "Ounces"],
        "conversions": {
            "Kilograms": 1,
            "Grams": 0.001,
            "Pounds": 0.453592,
            "Ounces": 0.0283495,
        },
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
        # Special handling for Temperature
    },
    "Volume": {
        "units": ["Liters", "Milliliters", "Gallons", "Cubic Meters", "Cubic Feet"],
        "conversions": {
            "Liters": 1,
            "Milliliters": 0.001,
            "Gallons": 3.78541,
            "Cubic Meters": 1000,
            "Cubic Feet": 28.3168,
        },
    },
    "Time": {
        "units": ["Seconds", "Minutes", "Hours", "Days", "Weeks"],
        "conversions": {
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
            "Weeks": 604800,
        },
    },
    "Area": {
        "units": ["Square Meters", "Square Kilometers", "Square Miles", "Square Feet", "Acres"],
        "conversions": {
            "Square Meters": 1,
            "Square Kilometers": 1000000,
            "Square Miles": 2589988.11,
            "Square Feet": 0.092903,
            "Acres": 4046.86,
        },
    },
}

# Set up the page
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter GIAIC")

# Select conversion category
category = st.selectbox("Select a category", list(unit_categories.keys()))

# Select source and target units
from_unit = st.selectbox("From", unit_categories[category]["units"])
to_unit = st.selectbox("To", unit_categories[category]["units"])

# Input value to convert
value = st.number_input("Enter value to convert", value=0.0)

# 🔁 Function to handle temperature conversion
def convert_temperature(value, from_u, to_u):
    if from_u == to_u:
        return value
    if from_u == "Celsius":
        if to_u == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_u == "Kelvin":
            return value + 273.15
    elif from_u == "Fahrenheit":
        if to_u == "Celsius":
            return (value - 32) * 5/9
        elif to_u == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_u == "Kelvin":
        if to_u == "Celsius":
            return value - 273.15
        elif to_u == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None

# Conversion logic
if category == "Temperature":
    result = convert_temperature(value, from_unit, to_unit)
else:
    from_rate = unit_categories[category]["conversions"][from_unit]
    to_rate = unit_categories[category]["conversions"][to_unit]
    result = value * from_rate / to_rate

# Display result
st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
