import streamlit as st

st.title("🔄 Unit Converter")

unit_categories = {
    "Length": {
        "units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "conversion": {
            "Meter": 1,
            "Kilometer": 1000,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254
        }
    },
    "Weight": {
        "units": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
        "conversion": {
            "Kilogram": 1,
            "Gram": 0.001,
            "Milligram": 0.000001,
            "Pound": 0.453592,
            "Ounce": 0.0283495
        }
    }
}

category = st.selectbox("Select Category", list(unit_categories.keys()))
units = unit_categories[category]["units"]
conversion = unit_categories[category]["conversion"]

from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
value = st.number_input("Enter value", min_value=0.0, format="%.4f")

if st.button("Convert"):
    result = value * conversion[from_unit] / conversion[to_unit]
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")