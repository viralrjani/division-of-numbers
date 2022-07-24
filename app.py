import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Division of 2 numbers
This app divide the 2 input number
""")
#Get Input

st.header('User Input Parameters')

number1 = st.number_input('Number1',min_value=0.0,max_value=9999999.0)
number2 = st.number_input('Number2',min_value=0.0,max_value=9999999.0)

if number2 != 0:
  Ans = number1 / number2
else:
  Ans = 0

st.subheader('Division of 2 Numbers')
st.write(Ans)

