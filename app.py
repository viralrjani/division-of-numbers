import streamlit as st

st.write("""
# Division of 2 numbers
This app divide the 2 input number
""")
#Get Input

st.header('User Input Parameters')

number1 = st.number_input('Number1')
number2 = st.number_input('Number2')

if number2 != 0:
  Ans = number1 / number2
else:
  Ans = 0

st.subheader('Division of 2 Numbers')
st.write(Ans)

