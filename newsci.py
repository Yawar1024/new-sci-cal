import streamlit as st
import math

# Title of the app
st.title("Scientific Calculator")

# Display the input fields for user to enter numbers
st.write("## Enter Numbers")

# Creating input fields
num1 = st.number_input("First number", value=0.0)
num2 = st.number_input("Second number (optional for some operations)", value=0.0)

# Display the available operations
st.write("## Select Operation")
operation = st.selectbox("Choose an operation", 
                         ["Addition", "Subtraction", "Multiplication", "Division", "Power", 
                          "Square Root", "Logarithm (Base 10)", "Sine", "Cosine", "Tangent"])

# Perform the operation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Division by zero is not allowed.")
        result = None
elif operation == "Power":
    result = num1 ** num2
elif operation == "Square Root":
    if num1 >= 0:
        result = math.sqrt(num1)
    else:
        st.error("Square root of negative number is not allowed.")
        result = None
elif operation == "Logarithm (Base 10)":
    if num1 > 0:
        result = math.log10(num1)
    else:
        st.error("Logarithm of non-positive number is not allowed.")
        result = None
elif operation == "Sine":
    result = math.sin(math.radians(num1))
elif operation == "Cosine":
    result = math.cos(math.radians(num1))
elif operation == "Tangent":
    result = math.tan(math.radians(num1))

# Display the result
if result is not None:
    st.write("## Result")
    st.write(f"The result of {operation.lower()} is: {result}")
