import streamlit as st
import math
import numpy as np

# Title of the app
st.title("Scientific Calculator")

# Create a text input box for the expression
expression = st.text_input("Enter expression", "")

# Calculator buttons in a grid layout
st.subheader("Basic Operations")
col1, col2, col3, col4 = st.columns(4)

# Basic operations
with col1:
    if st.button("sin(x)"):
        expression += "math.sin("
    if st.button("cos(x)"):
        expression += "math.cos("
    if st.button("tan(x)"):
        expression += "math.tan("

with col2:
    if st.button("log(x)"):
        expression += "math.log("
    if st.button("exp(x)"):
        expression += "math.exp("
    if st.button("sqrt(x)"):
        expression += "math.sqrt("

with col3:
    if st.button("x^y"):
        expression += "**"

    if st.button("("):
        expression += "("
    if st.button(")"):
        expression += ")"

with col4:
    if st.button("π"):
        expression += str(math.pi)
    if st.button("e"):
        expression += str(math.e)
    if st.button("Clear"):
        expression = ""

# Allow input of numbers and basic operators
expression = st.text_input("Expression", expression)

# Display the result when the user presses the "Calculate" button
if st.button("Calculate"):
    try:
        # Use eval to evaluate the expression safely
        result = eval(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

# Display additional mathematical constants and functions
st.subheader("Advanced Functions")
st.write("You can use additional functions like:")
st.write("`sin(x)`, `cos(x)`, `tan(x)`, `log(x)`, `exp(x)`, `sqrt(x)`")
st.write("Constants available: `π`, `e`")

